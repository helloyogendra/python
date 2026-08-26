# PySpark 4.1 feature: Arrow-native Python UDF (@arrow_udf)
# JIRA: SPARK-52214 | Released: Spark 4.1.0, Dec 2025
# https://spark.apache.org/releases/spark-release-4.1.0.html
#
# @arrow_udf runs directly on PyArrow arrays instead of plain Python
# objects or Pandas Series, skipping the Python-object / Pandas
# conversion step that regular @udf / @pandas_udf pay for.
#
# Requires: pyspark>=4.1, pyarrow
import pyarrow as pa
import pyarrow.compute as pc
from pyspark.sql import SparkSession
from pyspark.sql.functions import arrow_udf
from pyspark.sql.types import DoubleType

spark = SparkSession.builder.appName("arrow_native_udf_demo").getOrCreate()

df = spark.createDataFrame(
    [("Mango", 12.0), ("Banana", 3.5), ("Apple", 7.25)],
    schema=["fruit", "pricePerKg"],
)


@arrow_udf(DoubleType())
def apply_discount(price: pa.Array) -> pa.Array:
    # 10% discount, computed with vectorized PyArrow compute kernels
    return pc.multiply(price, pa.scalar(0.9))


df.withColumn("discountedPrice", apply_discount(df.pricePerKg)).show()

spark.stop()
