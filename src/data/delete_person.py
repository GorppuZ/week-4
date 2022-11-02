import psycopg2
from config import config

def delete_part(id):
    """ delete part by part id """
    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database 
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM person WHERE id = %s", (id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

def delete_part_certificates(id):
    """ delete part by part id """
    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM certificates WHERE id = %s", (id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted

if __name__ == '__main__':

    deleted_rows_c = delete_part_certificates(13)
    print('The number of deleted rows: ', deleted_rows_c)
    deleted_rows = delete_part(13)
    print('The number of deleted rows: ', deleted_rows)
