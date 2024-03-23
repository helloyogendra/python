from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import BooleanType

from spark_create_dataframe import create_dataframe, create_small_dataframe

df = create_dataframe()
df_small = create_small_dataframe()


def find_subset(df):

    window_spec = Window.orderBy(F.col("start").cast("long")).rangeBetween(0, 900)                          # working
    df_with_window = df.withColumn("group", F.collect_list("start").over(window_spec))

    # Create a lag column to compare with the previous group
    df_with_previous = df_with_window.withColumn("previous_group", F.lag("group").over(Window.orderBy("start")))

    # Define a UDF to check if one list is a subset of another
    def is_subset(current_group, previous_group):
        if previous_group is None:
            return False
        return set(current_group).issubset(set(previous_group))

    is_subset_udf = F.udf(is_subset, BooleanType())

    # Apply the UDF to create a new column
    df_final = df_with_previous.withColumn("is_subset_of_previous", is_subset_udf(F.col("group"), F.col("previous_group")))

    df_final.show(truncate=False)

    print("writing the csv file now ")

    df_new = df_final.toPandas()
    df_new.to_csv("groups.csv", index=False)
    print("check the grouped file")



find_subset(df_small)