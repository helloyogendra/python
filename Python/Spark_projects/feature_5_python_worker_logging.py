# PySpark 4.1 feature: structured logging from inside Python UDFs/workers
# JIRA: SPARK-53975 (worker logging), SPARK-53976 (logging in Pandas/Arrow UDFs)
# Released: Spark 4.1.0, Dec 2025
# https://spark.apache.org/releases/spark-release-4.1.0.html
#
# Log lines emitted with the standard `logging` module inside a UDF can
# now be enabled and pulled back onto the driver as a queryable
# DataFrame via python_worker_logs(), instead of only showing up in
# scattered executor stdout/stderr.
#
# NOTE: verify the exact python_worker_logs() call shape against the
# pyspark docs for your installed 4.1.x version - it may be a plain
# function, a SparkSession method, or a SQL table-valued function.
#
# Requires: pyspark>=4.1
import logging

from pyspark.sql import SparkSession
from pyspark.sql.functions import python_worker_logs, udf
from pyspark.sql.types import StringType

spark = SparkSession.builder.appName("worker_logging_demo").getOrCreate()
spark.conf.set("spark.sql.pyspark.worker.logging.enabled", "true")


@udf(StringType())
def grade_fruit_stock(qty: int) -> str:
    logger = logging.getLogger("fruit_grading")
    if qty < 50:
        logger.warning(f"low stock detected: qty={qty}")
        return "LOW_STOCK"
    logger.info(f"stock ok: qty={qty}")
    return "OK"


df = spark.createDataFrame(
    [("Mango", 120), ("Banana", 30), ("Apple", 80)],
    schema=["fruit", "qty"],
)

result = df.withColumn("stockStatus", grade_fruit_stock(df.qty))
result.show()

# Pull the log lines emitted inside the Python workers back as a DataFrame
python_worker_logs(spark).show(truncate=False)

spark.stop()
