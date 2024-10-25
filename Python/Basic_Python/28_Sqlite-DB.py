# Python - Database - sqlite

import sqlite3

def databaseFunction(db_name):
    conn = sqlite3.connect(db_name)
    print(f" {db_name} database connected")

    tableScript = "create table mytable (name text, age int, mobile int) "

    conn.execute(tableScript)
    print(f"table created")

    insertData = "insert into mytable values('Alex', 28, 652312)"

    conn.execute(insertData)
    print(f"data inserted")

    conn.commit()
    conn.close()


def insertData(tableName):
    conn = sqlite3.connect("sample.db")

    #conn.execute(f"create table {tableName} (name text, age int) ")

    conn.execute(f"insert into mytable values('Tom', 35, 454556)")

    conn.commit()
    conn.close()


choice = input("do you want to create a database? if yes type a name or just press enter  ")

if len(choice) > 1:
    databaseFunction(choice + ".db")


def getData(tableName):
    conn = sqlite3.connect("sample.db")

    selectScript = f"select * from {tableName}"

    cursor = conn.execute(selectScript)

    for rows in cursor:
       print(f"{rows[0]} - {rows[1]} - {rows[2]} ")
       #print(len(rows))
       
    conn.close()


tableName = "mytable"

#insertData(tableName)


def updateData():
    conn = sqlite3.connect("sample.db")

    conn.execute(f"update mytable set age=32 where name = 'Alex'")

    conn.commit()
    conn.close()


def deleteData():
    conn = sqlite3.connect("sample.db")

    conn.execute(f"delete from mytable where name = 'Alex'")

    conn.commit()
    conn.close()


getData(tableName)

deleteData()

getData(tableName)

#DML - Insert Data, Modify/Update Data, Delete Data
#CRUD - Create/Insert, Read/Select, Update/Modify, Delete
