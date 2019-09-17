#burn this mutha' down

import sqlite3
from sqlite3 import Error

db_file = "first_database.db"

#establish a connection to an existing db
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

#Makes a table in the db
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

 
# if __name__ == '__main__':
#     create_connection(r"/Users/fredricklambuth/Documents/Notes/PYTHON/sqlite/first_database.db")
