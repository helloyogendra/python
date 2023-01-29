# MySQL Database

# to connect with the MySQL database we need to install the connector library/package, refer below command to install
# python -m pip install mysql-connector-python
# Also, make sure your system has the mySQL Database Software, while installing remember the root user-name and password

import mysql.connector as ms

print("MySQL DB Examples")
#print(ms)


def connectServer():
    myDatabase = ms.connect(
                    host="localhost", 
                    user="root", 
                    passwd="James@001"
                )                         #if we are able to connect with the mySQL database server/instance, 'myDatabase' object will be initialized else error
    return myDatabase
                                           

def checkDatabase():
   
    myDatabase = connectServer()
    #print(myDatabase)

    myCursor = myDatabase.cursor(buffered=True)  # 'myDatabase' object is a connection object, we can use this to create a cursor object
                                                # cursor object will allow us to execute DB operation = create, insert, update, delete etc

    myCursor.execute("show databases")           #execute this command and get the list of available databases in mySQL Server

    db_list = []    #empty list

    for item in myCursor:
        db_list.append(list(item))

    #print(db_list)

    result = [str(val) for list1 in db_list for val in list1]

    print(result)                #print the lists of already available databases in the mysql server

    my_db_name = "training"

    if my_db_name in result:
        print(f"{my_db_name} database is already available in mySQL")
    else:
        myCursor.execute(f"create database {my_db_name}") 
        print(f"{my_db_name} create this database")

    myCursor.close()
    myDatabase.close()
    print("connection and cursor is closed!!")



#checkDatabase()

def connectDatabase():
    myConn = ms.connect(
                    host="localhost", 
                    user="root", 
                    passwd="James@001",
                    db = 'training'
                )                         #now we are connecting with a specific database,
    return myConn


# Function to create a new Table in the database
def creatingTables(query):
    try:
        conn = connectDatabase()
        print("conneted with the DB")

        cursor = conn.cursor(buffered=True)

        cursor.execute(query)
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()




# Function to insert the data in a table
def insertData(query, values):
    try:
        conn = connectDatabase()
        cursor = conn.cursor(buffered=True)
        cursor.execute(query, values)
        conn.commit()                       #must call the commit method to save the data in the table

        print(cursor.rowcount, " records inserted")
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()


# Function to get the data from a table
def selectData(query):
    try:
        conn = connectDatabase()
        cursor = conn.cursor(buffered=True)
        cursor.execute(query)

        result = cursor.fetchall()

        for data in result:
            print(data)


    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()


# Function to delete the data from a table
def deleteData(query):
    pass



insertQuery = "insert into secondTable(name, age, mobile) values (%s, %s, %s) "
values = ("John", 32, 12345)

createTableQuery = "create table secondTable (name varchar(20), mobile int, age int) "

selectQuery = "select * from secondtable "


#driver code to call those methods
if "y" == input("do you want to create a table, type-y  else press enter "):
    creatingTables(createTableQuery)
elif "i" == input("do you want to insert records in table, type-i else press enter "):
    insertData(insertQuery, values)
elif "r" == input("do you want to read records from table, type-r else press enter "):
    selectData(selectQuery)
else:
    print("no table created,  no data inserted, no data selected")





