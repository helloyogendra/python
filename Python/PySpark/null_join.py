import os
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

os.system("clear")

# Initialize a Spark session
spark = SparkSession.builder.appName("CreateDataFrame").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

# Define the schema of the DataFrame
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("sym", StringType(), True),
    StructField("trader_id", IntegerType(), True),
    StructField("qty", IntegerType(), True)
])

# Sample data with some null values in 'num' column
data_1 = [
    (1, "A", 101, 100),
    (1, "A1", 101, 100),
    (1, "A2", 101, 100),
    (1, "A3", 101, 100),
    (2, "B", None, 200),
    (3, "C", 201, 300),
]

data_2 = [
    (None, "B", None, 200),
    (2, "C", 201, 300),
    (3, "D", 201, 300),
]

# Create DataFrame with the defined schema and sample data
df_1 = spark.createDataFrame(data_1, schema)
df_2 = spark.createDataFrame(data_2, schema)

# Show the DataFrame
print("===========================================\n")
cols1 = ["d1."+cols for cols in df_1.columns]

result_df_1 = df_1.alias("d1").join(df_2.alias("d2"), df_1.id == df_2.id, "inner")
result_df_1 = result_df_1.select(*cols1)
result_df_1.show()

result_df_2 = df_1.join(df_2, df_1.id == df_2.id, "left")
result_df_2.show()
result_df_2.printSchema()

result_df_1.write.mode("overwrite").csv('./results.csv')
