import os
import pyspark.sql.functions as F
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark import SparkContext


os.system("clear")

# Initialize a Spark session
spark = SparkSession.builder.appName("CreateDataFrame").getOrCreate()

sc = SparkContext.getOrCreate()
conf = sc.getConf()
spark.sparkContext.setLogLevel("ERROR")

# Define the schema of the DataFrame
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("sym", StringType(), True),
    StructField("trader_id", IntegerType(), True),
    StructField("qty", IntegerType(), True)
])

# Sample data with some null values in 'num' column
data = [
    (1, "A", 101, 100),
    (2, "B", None, 200),
    (3, "C", 201, 300),
    (4, "D", None, 400),
    (5, "E", 401, 500),
    (6, "A", 101, 150),
    (7, "B", 601, 250),
    (8, "A", None, 350),
    (9, "F", None, 125),
    (10, "F", None, 135),
    (11, "F", 701, 135)
]

# Create DataFrame with the defined schema and sample data
df = spark.createDataFrame(data, schema)

# Show the DataFrame
print("===========================================\n")
df.show()

def aggregate_qty_by_sym(df):

    return df.groupBy("sym").agg(F.sum("qty").alias("total_qty"))

def aggregate_qty_by_sym_num(df):

    return df.groupBy("sym", "trader_id").agg(F.sum("qty").alias("total_qty"))


df_agg_by_sym = aggregate_qty_by_sym(df)


print("======================by sym=====================\n")
df_agg_by_sym.show()

df_agg_by_sym_num = aggregate_qty_by_sym_num(df)

print("======================by sym + trade_id=====================\n")
df_agg_by_sym_num.show()
