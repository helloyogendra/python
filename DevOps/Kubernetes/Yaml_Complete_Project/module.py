import os
import mysql.connector as ms

# we are loading system environment variables
# deployment (pod) will load the K8s-Secret and K8s-ConfigMap
# pass this info to cluster-ip service
# cluster-ip service will use this info to establish connection between python-code [in pod] and mysql-db [in pod]
# password which is mentioned in secret object is being used by both statefulset(pod) & deployment (pod)

hostname = os.getenv("DB_HOSTNAME", "localhost")  # load the name of cluster-ip service from config-map
port = int(os.getenv("DB_PORT", "3306"))          # port from config-map -> cluster-ip -> mysql-container/pod port
username = os.getenv("DB_USERNAME", "root")       # mostly root -> username from from config-map
password = os.getenv("DB_PASSWORD", "abcd")       # password from secret


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


