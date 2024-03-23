from pyspark.sql import functions as F
from pyspark.sql.window import Window
from pyspark.sql.types import TimestampType, BooleanType

from spark_create_dataframe import create_order_dataframe, get_color_codes, create_grouped_dataframe


_, G, _, _, RS = get_color_codes()

df = create_order_dataframe()


def order_by_two(df):

    # Define window specification
    windowSpec = Window.partitionBy("sym").orderBy(F.col("start").asc(), F.col("id").asc())

    # Add row number within each partition
    df = df.withColumn("row_num", F.row_number().over(windowSpec))

    # Filter to get the last row of each partition
    result_df = df.groupBy("sym").agg(F.max("row_num").alias("max_row_num")).join(df, ["sym"])\
                                        .filter(F.col("row_num") == F.col("max_row_num"))

    # Show the result
    result_df.show(truncate=False)

    print(result_df.columns)






order_by_two(df)
    
   

df_1 = create_grouped_dataframe()


def func_one(df_quotes):

    # Group by quoteReqID and find the maximum seqNum for each group
    
    df_quotes = df_quotes.orderBy(F.col("times").asc())

    df_quotes.show(truncate=False)

    max_seq_df = df_quotes.groupBy("id").agg(
        F.max("times").alias("max_times"),
        F.last("sym").alias("max_seqNum")
    )

    max_seq_df.show()

    max_seq_df_2 = max_seq_df.groupBy("id").agg(
        F.max("max_seqNum").alias("max_seqNum2"),
         F.first("max_times").alias("max_times2")
    )

    max_seq_df_2.show()

    # Join the original DataFrame with the max_seq_df to get the last quote for each quoteReqID
    # The join condition ensures that we match the maximum seqNum for each quoteReqID
    joined_df = df_quotes.alias("qt").join(max_seq_df.alias("mx"), 
                                        (F.col("qt.id") == F.col("mx.id")) & 
                                        (F.col("qt.sym") == F.col("mx.max_seqNum"))
                                    )

    # Filter out events with eventType as 'FILL' and non-null 'sym', and order by transactTime
    joined_df.show()



func_one(df_1)




