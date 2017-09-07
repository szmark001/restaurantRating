import sqlite3
from sqlite3 import Error
import Models

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        create_table(conn, 'CREATE TABLE User (user_id text PRIMARY KEY NOT NULL UNIQUE, first_name text NOT NULL, last_name text NOT NULL, phone text UNIQUE)')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_connection('restaurantRating.db')
