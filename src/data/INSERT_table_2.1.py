import psycopg2
from config import config

def insert_certificates():
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        cur.execute("""
...     INSERT INTO certificates (an_int, a_date, another_date, a_string)
...     VALUES (%(int)s, %(date)s, %(date)s, %(str)s);
...     """,
...     {'int': 10, 'str': "O'Reilly", 'date': datetime.date(2005, 11, 18)})



        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    insert_certificates()






>>> 