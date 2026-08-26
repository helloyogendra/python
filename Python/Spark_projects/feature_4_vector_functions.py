# PySpark 4.2 feature: native vector functions (vector_norm, vector_l2_distance)
# Released: Spark 4.2.0, Jul 2026
# https://downloads.apache.org/spark/docs/4.2.0-preview2/api/sql/vector-functions/
#
# New built-in SQL functions for working with float-array "vectors"
# directly in DataFrame expressions, without pulling in MLlib's Vector
# type - handy for similarity/distance style feature comparisons.
#
# Requires: pyspark>=4.2
from pyspark.sql import SparkSession
from pyspark.sql.functions import array, lit, vector_l2_distance, vector_norm

spark = SparkSession.builder.appName("vector_functions_demo").getOrCreate()

# Each row is a small feature vector describing a fruit: [sweetness, acidity, size]
df = spark.createDataFrame(
    [
        ("Mango", 8.0, 2.0, 7.0),
        ("Banana", 7.0, 1.0, 6.0),
        ("Apple", 5.0, 4.0, 5.0),
    ],
    schema=["fruit", "sweetness", "acidity", "size"],
).select("fruit", array("sweetness", "acidity", "size").alias("features"))

mango_profile = array(lit(8.0), lit(2.0), lit(7.0))  # used as the reference vector

(
    df.withColumn("l2Norm", vector_norm("features", lit(2.0)))
    .withColumn("distanceFromMango", vector_l2_distance("features", mango_profile))
    .orderBy("distanceFromMango")
    .show(truncate=False)
)

spark.stop()
