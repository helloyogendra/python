import mysql.connector as mysql

print("Trying to connect with the DB")

def checkDB():
    db = mysql.connect(host="localhost", port=3309, user="root", passwd="abcd1234")

    if db.is_connected():
        print("connected")
    else:
        print("not connected")

    cursor = db.cursor()
    cursor.execute("show databases;")

    for items in cursor:
        print(items)       

    cursor.close()


def connectToDatabase():
    db = mysql.connect(host="localhost", port=3309, user="root", passwd="abcd1234", db="docker")

    if db.is_connected():
        print("connected")
    else:
        print("not connected")

    cursor = db.cursor()
    cursor.execute("show tables;")

    for items in cursor:
        print(items)       

    cursor.close()


connectToDatabase()


# install below library in your local python environment/system
# pip install mysql-connector-python

# if we are going to run this python code within a container make sure-
# container is python based or python is installed
# above library is installed in this container


