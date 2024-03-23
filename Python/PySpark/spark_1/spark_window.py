from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col, expr

from pyspark.sql.window import Window
from pyspark.sql.types import StructType, StructField, IntegerType, TimestampType

# Fixed Window (Tumbling Window): [1-2-3] [4-5-6] [7-8-9] (No overlap)
# Sliding/Rolling/Moving Window (Size 3, Slide by 1): [1-2-3] [2-3-4] [3-4-5] [4-5-6] (Overlapping)

# Initialize Spark session
spark = SparkSession.builder.appName("app").getOrCreate()

# Sample data with id, timestamp, and value
data = [
    (1, "2023-10-27 15:01:24", "2023-10-27 15:15:24", 20),
    (1, "2023-10-27 15:05:24", "2023-10-27 15:10:24", 25),
    (1, "2023-10-27 15:06:24", "2023-10-27 15:20:24", 30),
    (2, "2023-10-27 15:20:24", "2023-10-27 15:35:24", 30),
    (2, "2023-10-27 15:40:24", "2023-10-27 15:58:24", 40),
    (3, "2023-10-27 16:01:24", "2023-10-27 16:17:24", 50),
    (1, "2023-10-27 16:17:24", "2023-10-27 16:35:24", 60),
]

columns = ["id","start", "end", "value"]

schema = StructType([
    StructField("id", IntegerType()),
    StructField("start", TimestampType()),
    StructField("end", TimestampType()),
    StructField("value", IntegerType())
])

# Create DataFrame
df = spark.createDataFrame(data, columns)
df.show(truncate=False)

# Ensure that the timestamp is in the correct format
time_format = "yyyy-MM-dd HH:mm:ss"
df = df.withColumn("start", F.to_timestamp(df["start"], time_format))
df = df.withColumn("end", F.to_timestamp(df["end"], time_format))

df = df.withColumn('start',df.start.astype('Timestamp').cast("long"))
ww = Window.partitionBy('id').orderBy('start').rangeBetween(0, 900)

# Define the sliding window
#windowSpec = Window.partitionBy("start", "end", "id").orderBy("start")#.rowsBetween(-2, Window.currentRow)
#windowSpec = Window.orderBy("start").rangeBetween(F.lit("0 seconds"), F.lit("15 minutes"))
# Calculate the sum over the window
df_with_sliding_sum = df.withColumn("sliding_sum", F.sum("value").over(ww))

# Show the resulting DataFrame
df_with_sliding_sum.show(truncate=False)

# Stop the Spark session



