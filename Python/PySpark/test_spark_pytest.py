import pytest
from pyspark.sql import SparkSession

@pytest.fixture
def spark():
    spark = SparkSession.builder.appName("Testing PySpark Example").getOrCreate()
    yield spark

def test_single_space(spark):
    

    sample_data = [{"name": "John    D.", "age": 30},
                   {"name": "Alice   G.", "age": 25},
                   {"name": "Bob  T.", "age": 35},
                   {"name": "Eve   A.", "age": 28}]

    # Create a Spark DataFrame
    original_df = spark.createDataFrame(sample_data)

    assert original_df is not None