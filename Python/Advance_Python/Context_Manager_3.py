# Context Manager
# Releasing Resource automatically

# Custom Context Manager for MySQL Database connections

# For this Example to work-
# Make sure that 'MySQL Database Server' is installed in your system
# Make sure that you installed below Python package - 
# pip install mysql-connector-python


# example
# MySQL and Python - without a context manager

import mysql.connector as ms
from contextlib import contextmanager                   # to create context manager


def connect_database_server():
    connection = ms.connect(
        host='localhost',
        user = 'root',
        passwd = 'James@001'
    )

    return connection


def print_database_list():

    conn = connect_database_server()
    cursor = conn.cursor()
    cursor.execute('show databases;')

    for items in cursor:
        print(items)

    cursor.close()
    conn.close()


print_database_list()



# example
# MySQL and Python - with a context manager

@contextmanager
def connect_db_server(host='localhost', user='root', password='James@001'):

    try:
        connection = ms.connect(host=host, user = user, passwd = password)

        if connection:
            print('Database connection is available')
            yield connection
        else:
            raise Exception('Database connection is not available')
    except Exception as ex:
        print('ex')
    finally:
        if connection:
            connection.close()
            print('Database connection is closed')
    



# using the above context manager

with connect_db_server() as conn:
   
    cursor = conn.cursor()
    cursor.execute('show databases;')

    for items in cursor:
        print(items)
