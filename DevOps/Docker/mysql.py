# Objective
# Connecting the Python code to database server running inside a docker container
# if container is running and port/other details are mentioned correctly, this code will work else it will not work

# Also, we need to install python dependency/package for MySQL
# pip install mysql-connector-python 

# test-1 : while docker container is running with an image of MySQL - expecting that it will work.
# test-2 : while docker container is not running - expecting that it will not work.

import os
import mysql.connector as ms

os.system('clear')

def test_mysql_connection():
    try:
        print("Testing MySQL DB connetion\n")

        sql_connect = ms.connect(
              database="docker",
              user = 'root',
              password="abc123",
              host="localhost",
              port="3333"
         )
        
        cursor = sql_connect.cursor()
        cursor.execute("Select version();")

        result = cursor.fetchone()

        print("MySQL Database Version is = ", result)

        cursor.execute("show variables where variable_name like 'version%' or variable_name like 'hostname%';")

        for x in cursor:
            print(x)


    except Exception as ex:
        print("Error in MySQL DB connetion - ", ex)
    else:
        print("MySQL DB connetion is available, we are good\n")
    finally:
        print("Closing the DB connetion\n")
        if cursor: cursor.close()
        if sql_connect: sql_connect.close()


# calling function
test_mysql_connection()