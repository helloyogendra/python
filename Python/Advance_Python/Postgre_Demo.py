# env_spark
# pip install psycopg2
# 
# 

import psycopg2
from psycopg2 import sql

def test_connection():
    try:
        print("Testing PostgreSQL Databse Connection from Python Code \n")

        # Connection parameters
        conn = psycopg2.connect(
            dbname="test",
            user="postgres",
            password="abc123",
            host="localhost",  # or the IP of your PostgreSQL server
            port="54322"  # default port for PostgreSQL
        )

        print("PostgreSQL Databse Connection is available!!\n")

        # Create a cursor object
        cur = conn.cursor()

        # Example query to check connection
        cur.execute("SELECT version();")

        # Fetch and print the result
        db_version = cur.fetchone()
        print(f"Connected to: {db_version}\n")

    except Exception as ex:
        print("PostgreSQL Databse Connection is not available - Test Failed!!")
        print("Error - ", ex)
    else:
        print("PostgreSQL Databse Connection is available - Test Success!!")
    finally:
        # Close the cursor and connection
        cur.close()
        conn.close()
        print("PostgreSQL Databse Connection is Closed")


test_connection()