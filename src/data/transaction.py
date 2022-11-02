import psycopg2
from config import config


def connect_db(amount, account_a, account_b):
    try:
        params = config()
        connection = psycopg2.connect(**params)
        connection.autocommit = False
        cursor = connection.cursor()

        query = """select balance from account where account_a = %s"""
        cursor.execute(query, account_a)
        record = cursor.fetchone()[0]
        balance_account_A = int(record)
        balance_account_A -= amount

        # Withdraw from account A  now
        sql_update_query = """Update account set balance = %s where account_a = %s"""
        cursor.execute(sql_update_query, (balance_account_A,))

        query = """select balance from account where account_b = %s"""
        cursor.execute(query, account_b)
        record = cursor.fetchone()[0]
        balance_account_B = int(record)
        balance_account_B += amount

        # Credit to  account B  now

        sql_update_query = """Update account set balance = %s where account_b = %s"""
        cursor.execute(sql_update_query, (balance_account_B,))

        # commiting both the transction to database
        connection.commit()
        print("Transaction completed successfully ")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error in transction Reverting all other operations of a transction ", error)
        connection.rollback()

    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
    

    if __name__ == '__main__':
        connect_db(2500, 624001562408, 2236781258763)