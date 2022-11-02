from typing import Any
import psycopg2
from config import config

def insert_certificates(name, person_id):
#def insert_person(vendor_list):
    
    conn = None
    try:
        # read database configurationm
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO certificates(name, person_id) VALUES(%s, %s);
        """,
        (name, person_id)
        )
        # execute the INSERT statement
        #cur.executemany(sql,vendor_list)
        # commit the changes to the database
        conn.commit()
        print('done')
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_person(name, age):
#def insert_person(vendor_list):
    """ insert multiple vendors into the vendors table  """

    conn = None
    try:
        # read database configurationm
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        cur.execute("""
        INSERT INTO person(name, age) VALUES(%s, %s)
        """,
        (name, age)
        )
        # execute the INSERT statement
        #cur.executemany(sql,vendor_list)
        # commit the changes to the database
        conn.commit()
        print('done too')
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    insert_certificates('SCRUM', 16)
    # insert one vendor
    insert_person('Gogo', 55)
    # insert multiple vendors
    #insert_vendor_list([
        #('Harry', 12),
        #('Ron', 30),
        #('Hagrid', 90),
    #])