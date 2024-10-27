### 1. **Define the Repository Interface**
# Start by defining an abstract base class, `DataRepository`, 
# which will serve as the interface for any concrete repository that interacts with PostgreSQL.


import json
from abc import ABC, abstractmethod
from pyspark.sql import SparkSession, DataFrame, Row


class DataRepository(ABC):
    @abstractmethod
    def save(self, dataframe: DataFrame, table_name: str):
        """Save DataFrame to the database."""
        pass

    @abstractmethod
    def load(self, table_name: str) -> DataFrame:
        """Load data from the database into a DataFrame."""
        pass


### 2. Implement a PostgreSQL Repository
# This concrete repository uses PySpark’s 
# JDBC support to save and load data to and from PostgreSQL. 
# It handles serialization and deserialization to JSON, 
# saving JSON data into the specified table in PostgreSQL.


class PostgresDataRepository(DataRepository):
    def __init__(self, spark: SparkSession, jdbc_url: str, db_properties: dict):
        self.spark = spark
        self.jdbc_url = jdbc_url
        self.db_properties = db_properties

    def save(self, dataframe: DataFrame, table_name: str):
        """Save DataFrame as JSON to the PostgreSQL table."""
        dataframe.write.jdbc(
            url=self.jdbc_url,
            table=table_name,
            mode="append",
            properties=self.db_properties
        )
        print(f"Data saved to PostgreSQL table: {table_name}")

    def load(self, table_name: str) -> DataFrame:
        """Load JSON data from PostgreSQL and return as DataFrame."""
        dataframe = self.spark.read.jdbc(
            url=self.jdbc_url,
            table=table_name,
            properties=self.db_properties
        )
        print(f"Data loaded from PostgreSQL table: {table_name}")
        return dataframe


### 3. **Implement Serialization and Deserialization Helper Methods**
# If JSON serialization/deserialization is required for data 
# before saving to or after loading from PostgreSQL, 
# you can add helper functions in the repository.


class PostgresDataRepository(DataRepository):
    def __init__(self, spark: SparkSession, jdbc_url: str, db_properties: dict):
        self.spark = spark
        self.jdbc_url = jdbc_url
        self.db_properties = db_properties

    def save(self, dataframe: DataFrame, table_name: str):
        # Save data as JSON strings in the database
        json_df = dataframe.toJSON().toDF("json_data")
        json_df.write.jdbc(
            url=self.jdbc_url,
            table=table_name,
            mode="append",
            properties=self.db_properties
        )
        print(f"JSON data saved to PostgreSQL table: {table_name}")

    def load(self, table_name: str) -> DataFrame:
        # Load JSON data and parse back to DataFrame rows
        json_df = self.spark.read.jdbc(
            url=self.jdbc_url,
            table=table_name,
            properties=self.db_properties
        )
        parsed_df = self.spark.read.json(json_df.rdd.map(lambda row: row.json_data))
        print(f"JSON data loaded from PostgreSQL table: {table_name}")
        return parsed_df


### 4. **Using the Repository in the Application**
# Here’s how you can use `PostgresDataRepository` to save and load data in your application.
# Set up the Spark session and database properties


spark = SparkSession.builder.appName("DataProcessingApp").getOrCreate()
jdbc_url = "jdbc:postgresql://localhost:5432/mydb"
db_properties = {
    "user": "myuser",
    "password": "mypassword",
    "driver": "org.postgresql.Driver"
}

# Create the repository instance
repository = PostgresDataRepository(spark, jdbc_url, db_properties)

# Example data
data = [("A101", 1000), ("B202", 2000)]
df = spark.createDataFrame(data, ["product_id", "revenue"])

# Save the data
repository.save(df, "processed_data")

# Load the data back
loaded_df = repository.load("processed_data")
loaded_df.show()

