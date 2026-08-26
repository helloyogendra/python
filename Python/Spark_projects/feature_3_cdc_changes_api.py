# PySpark 4.2 feature: Change Data Capture (CDC) changes() API
# JIRA: SPARK-55950 (Python API), SPARK-55668 (umbrella SPIP)
# Released: Spark 4.2.0, Jul 2026
# https://spark.apache.org/releases/spark-release-4-2-0.html
#
# Spark 4.2 adds a first-class way to read row-level changes (inserts,
# updates, deletes) from any DSv2 connector that exposes a change feed,
# via a new SQL `CHANGES` clause and matching DataFrame/PySpark APIs.
#
# NOTE: this only works against a CDC-capable table format - this demo
# uses Delta Lake with change data feed enabled. Requires: pyspark>=4.2,
# delta-spark, and the table format support for CDC to actually be
# installed/configured in your environment.
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("cdc_changes_demo")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config(
        "spark.sql.catalog.spark_catalog",
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",
    )
    .getOrCreate()
)

spark.sql("""
    CREATE TABLE IF NOT EXISTS fruit_stock (fruit STRING, qty INT)
    USING DELTA
    TBLPROPERTIES (delta.enableChangeDataFeed = true)
""")

spark.sql("INSERT INTO fruit_stock VALUES ('Mango', 120), ('Banana', 300)")
spark.sql("UPDATE fruit_stock SET qty = 90 WHERE fruit = 'Mango'")
spark.sql("DELETE FROM fruit_stock WHERE fruit = 'Banana'")

# New in Spark 4.2: read row-level changes with the changes() DataFrame API
changes_df = spark.read.option("startingVersion", 0).changes("fruit_stock")
changes_df.show()

# Equivalent using the new SQL CHANGES clause
spark.sql("SELECT * FROM fruit_stock CHANGES FROM VERSION 0").show()

spark.stop()
