from typing import Any
import psycopg2
from config import config

#!/usr/bin/python

import psycopg2
from config import config


def update_person(name, age, id):
    """ update person name based on the person id """
    sql = """ UPDATE person
                SET name = %s, age = %s
                WHERE id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (name, age, id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows

def update_certificates(name, person_id):
    """ update certificates name based on the person id """
    sql = """ UPDATE certificates
                SET name = %s
                WHERE person_id = %s"""
    conn = None
    updated_rows = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql, (name, person_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows    

if __name__ == '__main__':
    # Update vendor id 1
    update_person('Kalle', 100, 2)
    update_certificates('Google', 2)
    
    # insert multiple vendors
    #insert_vendor_list([
        #('Harry', 12),
        #('Ron', 30),
        #('Hagrid', 90),
    #])