# MySQL Database

import mysql.connector as ms

                                           
#Function to establish connection with database
def connectDatabase():
    myConn = ms.connect(
                    host="localhost", 
                    user="root", 
                    passwd="James@001",
                    db = 'training'
                )                         #now we are connecting with a specific database,
    return myConn


# Function to delete a Table in the database
def deleteTable(tableName):

    deleteTableQuery = f"drop table if exists {tableName} "

    try:
        conn = connectDatabase()
        cursor = conn.cursor()
        cursor.execute(deleteTableQuery)
        print(f"delete the table {tableName}")
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()


# Function to delete a Table in the database
def deleteTableData(query):
    try:
        conn = connectDatabase()
        print("conneted with the DB")

        cursor = conn.cursor()

        cursor.execute(query)
        conn.commit()
        print(cursor.rowcount, " record(s) deleted")
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()



# Function to insert the data in a table
def bulkInsertData(query, values):
    try:
        conn = connectDatabase()
        cursor = conn.cursor(buffered=True)
        cursor.executemany(query, values)           #observe this method here for bulk insert
        conn.commit()                               #must call the commit method to save the data in the table

        print(cursor.rowcount, " records inserted")
    except Exception as ex:
        print(f"Error:: {ex}")
    finally:
        cursor.close()
        conn.close()


# Function to update the data of a table
def updateData(query):
    try:
        conn = connectDatabase()
        cursor = conn.cursor(buffered=True)
        cursor.execute(query)

        conn.commit()
        print(cursor.rowcount, " record(s) updated")
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()



insertQuery = "insert into secondTable(name, age, mobile) values (%s, %s, %s) "
values = [
            ("John", 27, 12345),
            ("Alex", 33, 12121),
            ("Rob", 31, 12999),
            ("Bob", 32, 12444),
            ("Tim", 32, 12222),
            ("Tom", 35, 12111),
]

selectQuery = "select * from secondtable "
updateDataQuery = "update secondTable set age=30 where name = 'Alex'"
deleteDataQuery = "delete from secondTable where name = 'John'"


#driver code to call those methods
if "d" == input("do you want to delete a table, type-d  else press enter "):
    tableName = input("type the name of table to delete- ")
    deleteTable(tableName)
elif "i" == input("do you want to bulk insert records in table, type-i else press enter "):
    bulkInsertData(insertQuery, values)
elif "u" == input("do you want to update records from table, type-u else press enter "):
    updateData(updateDataQuery)
elif "x" == input("do you want to delete records from table, type-x else press enter "):
    deleteTableData(deleteDataQuery)
else:
    print("table operation cancelled")





