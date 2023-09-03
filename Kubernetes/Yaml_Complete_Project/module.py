import os
import mysql.connector as ms


hostname = os.getenv("DB_HOSTNAME", "localhost")
port = int(os.getenv("DB_PORT", "3306"))
username = os.getenv("DB_USERNAME", "root")
password = os.getenv("DB_PASSWORD", "abcd")


def checkDBConnection():
    try:
        connect = ms.connect(host=hostname, port=port, user=username, password=password)
        return True
    except Exception as ex:
        return False


def showDatabases():
    try:
        db_list = []
        db_names = ""

        connect = ms.connect(host=hostname, port=port, user=username, password=password)
        cursor = connect.cursor()
        cursor.execute('show databases;')

        for items in cursor:
            for values in items:
                db_list.append(values)
        
        db_names = str(db_list)
        return db_names
    except Exception as ex:
        return ex


