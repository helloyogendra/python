from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import TimestampType, BooleanType

from spark_create_dataframe import create_dataframe, get_color_codes, create_small_dataframe


_, G, _, _, RS = get_color_codes()

df = create_dataframe()

# Working
def grouping_by_window(df):

    window_spec = Window.orderBy("start_long").rangeBetween(0, 900)                
    df_with_sliding_sum = df.withColumn("sliding_sum", F.sum("value").over(window_spec))
    
    print(f"{G}Window.orderBy('start_long').rangeBetween(0, 900){RS} ")
    df_with_sliding_sum.show(truncate=False)





def grouping_by(df):

    group_cols = ["id"]
    grouped_df = df.groupBy(group_cols).agg(F.sum("value").alias("total"))

    print(f"{G}df.groupBy(group_cols).agg(F.sum('value').alias('total')){RS}")
    grouped_df.show(truncate=False)






def grouping_by_range(df):

    w = Window.orderBy("start_long").partitionBy("id").rangeBetween(-900, 900)
    new_df = df.withColumn("window_sum", F.sum("value").over(w))     

    print(f"{G}Window.orderBy('start_long').partitionBy('id').rangeBetween(0, 900){RS}")

    new_df = new_df.withColumn("unique_id", F.monotonically_increasing_id())
    new_df.show(truncate=False)





def group_by_range_and_window(df):
    
    result_df = df.groupBy("id" , F.window("start", "15 minutes")).sum("value").alias("total")

    print(f"{G}df.groupBy('id' , F.window('start', '15 minutes')).sum('value').alias('total'){RS}")
    result_df.show(truncate=False)



small_df = create_small_dataframe()



def new_logic(df):

    df = df.withColumn("timestamp_seconds", F.unix_timestamp("start"))

    # Define the window specification using the converted timestamp
    windowSpec = Window.partitionBy("id").orderBy("timestamp_seconds").rangeBetween(0, 15*60)

    # Apply your desired aggregation function within the window
    # For example, to calculate the sum of a column named 'value' within each 15-minute forward-looking window
    aggregated_df = df.withColumn("sum_value", F.sum("value").over(windowSpec))
    aggregated_df.show(truncate=False)




def rolling_window(df):

    # Self-join with a 15-minute window condition
    joined_df = df.alias("df1").join(df.alias("df2"), 
                                    (F.col("df1.id") == F.col("df2.id")) &
                                    (F.col("df2.start") >= F.col("df1.start")) &
                                    (F.col("df2.start") <= F.col("df1.end")))

    # Group by 'id' and the 'start' of the first DataFrame, and then aggregate
    aggregated_df = joined_df.groupBy("df1.start", "df1.end", "df1.id").agg(F.sum("df2.value").alias("sum_value"))

    # Show result
    aggregated_df.show()





def rolling_window_2(df):

    df = df.withColumn("start", F.unix_timestamp(F.col("start"), "HH:mm:ss").cast(TimestampType()))

    # Add an 'end' column that is 15 minutes after 'start'
    df = df.withColumn("end", F.col("start") + F.expr("INTERVAL 15 MINUTES"))

    # Self-join with the condition that 'start' of df2 falls within the 'start' and 'end' of df1
    joined_df = df.alias("df1").join(df.alias("df2"), 
                                    (F.col("df1.id") == F.col("df2.id")) &
                                    (F.col("df2.start") >= F.col("df1.start")) &
                                    (F.col("df2.start") <= F.col("df1.end")))

    # Group by 'id' and the 'start' of the first DataFrame, then aggregate
    aggregated_df = joined_df.groupBy("df1.start", "df1.id").agg(F.sum("df2.value").alias("sum_value"))

    # Show the result
    aggregated_df.show()




# best solution so far - 05-Dec-2023 - aggregation within window but without subset removal - also we are using unix-timestamp
def rolling_window_3(df):
    df = df.withColumn("start", F.unix_timestamp(F.col("start"), "HH:mm:ss").cast(TimestampType()))

    # Add an 'end' column that is 15 minutes after 'start'
    df = df.withColumn("end", F.col("start") + F.expr("INTERVAL 15 MINUTES"))

    # Self-join with the condition that 'start' of df2 falls within the 'start' and 'end' of df1
    # Note: We remove the condition that matches 'id' between df1 and df2
    joined_df = df.alias("df1").join(df.alias("df2"), 
                                    (F.col("df2.start") >= F.col("df1.start")) &
                                    (F.col("df2.start") < F.col("df1.end")))

    # Group by 'id' and the 'start' of the first DataFrame, then aggregate
    # Note: We are grouping by 'df1.start' and 'df2.id' to get the aggregation for each 'id' in the window starting from 'df1.start'
    aggregated_df = joined_df.groupBy("df1.start", "df2.id").agg(F.sum("df2.value").alias("sum_value"))

    # Show the result
    aggregated_df.show()
    aggregated_df = aggregated_df.groupBy("start", "id").agg(F.first("start"), F.first("id"))
    aggregated_df.show()


rolling_window_3(small_df)




@F.udf(BooleanType())
def is_subset(current_set, previous_set):
    if not previous_set:
        return False
    return set(current_set).issubset(set(previous_set))



def rolling_window_4(df):

    # Assuming df is your DataFrame
    # Convert 'start' to a timestamp type
    df = df.withColumn("start", F.unix_timestamp(F.col("start"), "HH:mm:ss").cast(TimestampType()))

    # Add an 'end' column that is 15 minutes after 'start'
    df = df.withColumn("end", F.col("start") + F.expr("INTERVAL 15 MINUTES"))

    # Self-join with the condition that 'start' of df2 falls within the 'start' and 'end' of df1
    joined_df = df.alias("df1").join(df.alias("df2"), 
                                    (F.col("df2.start") >= F.col("df1.start")) &
                                    (F.col("df2.start") < F.col("df1.end")))

    # Define a window specification partitioned by 'id' and ordered by 'start'
    windowSpec = Window.partitionBy("df1.id").orderBy("df1.start").rangeBetween(Window.unboundedPreceding, 0)

    # Create a new column 'max_end_so_far' for each 'id'
    joined_df = joined_df.withColumn("max_end_so_far", F.max("df2.end").over(windowSpec))

    # Mark rows as subset if their 'end' is less than or equal to 'max_end_so_far'
    joined_df = joined_df.withColumn("is_subset", (F.col("df2.end") <= F.col("max_end_so_far")) & (F.col("df1.start") != F.col("df1.end")))

    # Filter out subset rows
    non_subset_df = joined_df.filter(~F.col("is_subset"))

    # Perform the aggregation on the filtered DataFrame
    aggregated_df = non_subset_df.groupBy("df1.start", "df2.id").agg(F.sum("df2.value").alias("sum_value"))

    # Show the result
    aggregated_df.show()





        




rolling_window_4(small_df)