from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col, expr

from pyspark.sql.window import Window
from pyspark.sql.types import StructType, StructField, IntegerType, TimestampType

# Fixed Window (Tumbling Window): [1-2-3] [4-5-6] [7-8-9] (No overlap)
# Sliding/Rolling/Moving Window (Size 3, Slide by 1): [1-2-3] [2-3-4] [3-4-5] [4-5-6] (Overlapping)

# Initialize Spark session
spark = SparkSession.builder.appName("trim_string").getOrCreate()

# Sample data with id, timestamp, and value
data = [
    (1, "2023-10-27 15:01:24", 10),
    (2, "2023-10-27 15:05:24", 20),
    (3, "2023-10-27 15:09:24", 30),
    (4, "2023-10-27 15:13:24", 40),
    (5, "2023-10-27 15:17:24", 50),
    (6, "2023-10-27 15:21:24", 60),
]

columns = ["id","timestamp", "value"]

schema = StructType([
    StructField("id", IntegerType()),
    StructField("timestamp", TimestampType()),
    StructField("value", IntegerType())
])

# Create DataFrame
df = spark.createDataFrame(data, columns)
df.show(truncate=False)

# Ensure that the timestamp is in the correct format
time_format = "yyyy-MM-dd HH:mm:ss"
df = df.withColumn("timestamp", F.to_timestamp(df["timestamp"], time_format))

# Define the sliding window
windowSpec = Window.orderBy("timestamp").rowsBetween(-2, Window.currentRow)

# Calculate the sum over the window
df_with_sliding_sum = df.withColumn("sliding_sum", F.sum("value").over(windowSpec))

# Show the resulting DataFrame
df_with_sliding_sum.show(truncate=False)

# Stop the Spark session



