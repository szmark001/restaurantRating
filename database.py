import sqlite3
from sqlite3 import Error
import Models

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def construct_query(table, query_model):
    query = 'CREATE TABLE'
    query += ' ' + table
    query += '('
    for column in query_model:
        query += column + ' ' + query_model[column]['type']
        if query_model[column]['options']:
            query += ' ' + query_model[column]['options']
        query += ','
    if query[len(query)-1] == ',':
        query = query[:len(query)-1]
    query += ')'
    return query


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    try:
        conn = sqlite3.connect(db_file)
        for table in Models.models:
            create_table(conn, construct_query(table, Models.models[table]))
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_connection('restaurantRating.db')
