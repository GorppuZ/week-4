import psycopg2
from config import config

def get_certificates():
    """ query data from the vendors table """
    conn = None
    try:

        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT * FROM certificates")
        
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()
        cur.execute("SELECT * FROM certificates")
        column_names = [desc[0] for desc in cur.description]
        for i in column_names:
            print(i)
        conn.commit()
        

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
    get_certificates()

  
  
