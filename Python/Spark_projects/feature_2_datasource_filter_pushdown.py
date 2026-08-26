# PySpark 4.1 feature: filter pushdown for the Python Data Source API
# JIRA: SPARK-51271 | Released: Spark 4.1.0, Dec 2025
# https://spark.apache.org/releases/spark-release-4.1.0.html
#
# A DataSourceReader can now implement pushFilters(filters) to accept
# filters itself and only return the ones it can't handle, so Spark
# skips re-filtering rows it already knows are correct.
#
# NOTE: the exact shape of the Filter objects passed to pushFilters()
# is new in 4.1 - double check field names (e.g. `attribute`/`value`)
# against the pyspark.sql.datasource docs for your installed version.
#
# Requires: pyspark>=4.1
from pyspark.sql import SparkSession
from pyspark.sql.datasource import DataSource, DataSourceReader

FRUIT_STOCK = [
    ("Mango", "Fruit", 120),
    ("Banana", "Fruit", 300),
    ("Apple", "Fruit", 80),
    ("Carrot", "Vegetable", 200),
]


class FruitStockReader(DataSourceReader):
    def __init__(self):
        self.accepted_categories = None

    def pushFilters(self, filters):
        unhandled = []
        for f in filters:
            if getattr(f, "attribute", None) == "category" and hasattr(f, "value"):
                self.accepted_categories = self.accepted_categories or set()
                self.accepted_categories.add(f.value)
            else:
                unhandled.append(f)  # let Spark filter this one itself
        return unhandled

    def read(self, partition):
        for fruit, category, qty in FRUIT_STOCK:
            if self.accepted_categories is None or category in self.accepted_categories:
                yield (fruit, category, qty)


class FruitStockDataSource(DataSource):
    @classmethod
    def name(cls):
        return "fruitstock"

    def schema(self):
        return "fruit string, category string, qty int"

    def reader(self, schema):
        return FruitStockReader()


spark = SparkSession.builder.appName("datasource_filter_pushdown_demo").getOrCreate()
spark.dataSource.register(FruitStockDataSource)

df = spark.read.format("fruitstock").load().filter("category = 'Fruit'")
df.explain(True)  # shows the filter was pushed into FruitStockReader
df.show()

spark.stop()
