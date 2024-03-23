from functools import reduce
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("DynamicFilterExample").getOrCreate()

# Sample DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 22), ("David", 35)]
columns = ["name", "age"]
df = spark.createDataFrame(data, columns)

# Define dynamic filter conditions
filter_conditions = [
    ("age", ">", 25),
    ("name", "like", "C%"),
    # Add more dynamic conditions as needed
]
print("=============================================================")
print(filter_conditions)
print(type(filter_conditions))
print("=============================================================")
# Build the dynamic filter expression
dynamic_filter = reduce(lambda acc, condition: acc & (col(condition[0]) + condition[1] + condition[2]), filter_conditions, col("name").isNotNull())

print("=============================================================")
print(dynamic_filter)
print(type(dynamic_filter))
print("=============================================================")

# Apply the dynamic filter to the DataFrame
filtered_df = df.filter(dynamic_filter)

# Show the result
filtered_df.show()
