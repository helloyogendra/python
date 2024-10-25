from pyspark.sql import functions as F
from pyspark.sql.types import TimestampType, BooleanType
from pyspark.sql.window import Window

from spark_create_dataframe import create_dataframe, create_small_dataframe

df = create_dataframe()
df_small = create_small_dataframe()


def rolling_window_3(df):
    df = df.withColumn("start", F.unix_timestamp(F.col("start"), "HH:mm:ss").cast(TimestampType()))
    df = df.withColumn("end", F.col("start") + F.expr("INTERVAL 15 MINUTES"))

    # Use find_subset function to add 'is_subset_of_previous' column
    df = find_subset(df)

    # Filter out rows that are part of subset windows
    df = df.filter(~F.col("is_subset_of_previous"))

    # Perform the join and aggregation
    joined_df = df.alias("df1").join(df.alias("df2"), 
                                     (F.col("df2.start") >= F.col("df1.start")) &
                                     (F.col("df2.start") < F.col("df1.end")))
    aggregated_df = joined_df.groupBy("df1.start", "df2.id").agg(F.sum("df2.value").alias("sum_value"))
    return aggregated_df

def find_subset(df):
    window_spec = Window.orderBy(F.col("start").cast("long")).rangeBetween(0, 900)                         
    df_with_window = df.withColumn("group", F.collect_list("start").over(window_spec))

    df_with_previous = df_with_window.withColumn("previous_group", F.lag("group").over(Window.orderBy("start")))

    def is_subset(current_group, previous_group):
        if previous_group is None:
            return False
        return set(current_group).issubset(set(previous_group))

    is_subset_udf = F.udf(is_subset, BooleanType())

    df_final = df_with_previous.withColumn("is_subset_of_previous", is_subset_udf(F.col("group"), F.col("previous_group")))
    return df_final

# Assuming 'df' is your initial DataFrame
aggregated_df = rolling_window_3(df_small)
aggregated_df.show()
