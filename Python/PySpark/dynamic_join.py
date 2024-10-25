import os
import time
from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from spark_create_dataframe import create_order_dataframe

import py4j.protocol  
from py4j.protocol import Py4JJavaError  
from py4j.java_gateway import JavaObject  
from py4j.java_collections import JavaArray, JavaList

from pyspark import RDD, SparkContext  
from pyspark.serializers import PickleSerializer, AutoBatchedSerializer
from pyspark import SparkContext

os.system("clear")

df1: DataFrame = create_order_dataframe()
df2: DataFrame = create_order_dataframe()

rdd_1 = df1.rdd
rdd_1.persist()

df1.cache()
df2.cache()

# Helper function to convert python object to Java objects
def _to_java_object_rdd(rdd):  
    """ Return a JavaRDD of Object by unpickling
    It will convert each Python object into Java object by Pyrolite, whenever the
    RDD is serialized in batch or not.
    """
    rdd = rdd._reserialize(AutoBatchedSerializer(PickleSerializer()))
    return rdd.ctx._jvm.org.apache.spark.mllib.api.python.SerDe.pythonToJava(rdd._jrdd, True)


sc = SparkContext.getOrCreate()

# First you have to convert it to an RDD 
obj = _to_java_object_rdd(df1.rdd)

# Now we can run the estimator
print("-------------------get the df size------------------------------- \n")
sc._jvm.org.apache.spark.util.SizeEstimator.estimate(obj)
print("--------------------------get the df size------------------------- \n")
sc._jvm.org.apache.spark.util.SizeEstimator.estimate(df1._jdf)
print("------------------------------------------------------------------ \n")



def dynamic_join(df1: DataFrame, df2: DataFrame, join_columns: list, join_type: str = "inner") -> DataFrame:
    # Build the join condition dynamically based on the join_columns list
    if not join_columns:
        raise ValueError("Join columns list cannot be empty")

    df1_alias = "df1"
    df2_alias = "df2"
    df1 = df1.alias("df1")
    df2 = df2.alias("df2")

    # Start with the first join condition
    join_condition = F.col(f"{df1_alias}.{join_columns[0]}") == F.col(f"{df2_alias}.{join_columns[0]}")

    # Add additional join conditions for the rest of the columns in the list
    for col in join_columns[1:]:
        join_condition = join_condition & (F.col(f"{df1_alias}.{col}") == F.col(f"{df2_alias}.{col}"))


    print("join condition is : ", join_condition)

    # Perform the join
    return df1.join(df2.alias("df2"), on=join_condition, how=join_type)


print(df1.columns)
print(df2.columns)

# Example usage
join_columns_1 = ["sym"]  # Replace with your column names
joined_df_1 = dynamic_join(df1, df2, join_columns_1, "inner")
print(joined_df_1.count())


join_columns_2 = ["sym", "id"] 
joined_df_2 = dynamic_join(df1, df2, join_columns_2, "inner")
print(joined_df_2.count())

time.sleep(600)
