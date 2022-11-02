import psycopg2
from config import config

def get_person():
    """ query data from the vendors table """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM person")
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
    get_person()