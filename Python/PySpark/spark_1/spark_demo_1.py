import os
import math
import time
import logging
import asyncio
import pyspark.pandas as pd
from datetime import datetime
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.window import Window
from pyspark.sql import functions as F
from concurrent.futures import ThreadPoolExecutor

spark = None

def process_data():
    try:
        start_time = time.perf_counter()
        sc = SparkContext.getOrCreate()
        conf = sc.getConf()


        print("===================Spark Context Memory=======================================================")
        conf.set("spark.driver.memory", "2g")
        conf.set("spark.executor.memory", "4g")
        
        print("==============================================================================================")

        driver_memory =conf.get("spark.driver.memory")
        ex_memory = conf.get("spark.executor.memory")
        

        print(f"Spark Context Memory :: spark.driver.memory = {driver_memory}, spark.executor.memory={ex_memory}")
    

        print("================================================================================================")

        spark = SparkSession.builder.appName("app").getOrCreate()
        spark.sparkContext.setLogLevel("ERROR")

        file_path = "/home/hello/NIFTY50_all.csv"

        df = spark.read.csv(file_path, header=True, inferSchema=True)

        print("================================================================================================")
        print("================================================================================================")
        if df:
            print("data loaded")
            print("Dataframe columns are ", df.columns)
            print("Schema is ", df.printSchema())
            print("Nifty Fifty Count is = ", df.count())
        else:
            print(" no data loaded ")
        print("================================================================================================")
        if df and not df.isEmpty():
            print("dataframe is not empty")
            df.show(2)
        print("================================================================================================")

        df_filter = df.filter(df.Date >= "2020-01-01")
        asyncio.run(async_csv_write("filtered_data.csv", df_filter, "yes"))    # because this function call is asynchronous, it will not wait here for file writing to be complete.
        # Group by Symbol
        grouped_df = df_filter.groupBy("Symbol").sum("High")
        asyncio.run(async_csv_write("grouped_data.csv", grouped_df, "yes"))


        # Define a window specification and Calculate Sum for each Symbol
        windowSpec = Window.partitionBy("Symbol").orderBy("Date")
        window_df = df_filter.withColumn("New_High", F.sum("High").over(windowSpec))
        asyncio.run(async_csv_write("window_df.csv", window_df, "yes"))

        spark.range(10).show()
        partition = conf.get("spark.default.parallelism")
        print(f"Spark Partition :: spark.partition = {partition}")
        
        #time.sleep(82)
        end_time = time.perf_counter()
        time_unit = str( round( (end_time - start_time) / 60, 2) ) + " Minutes" if end_time - start_time >= 60 else str(end_time - start_time) + " Seconds"
        print(spark.sparkContext.getConf().getAll())
        print(f"Spark Data Run completed in {time_unit}")
        
    except Exception as ex:
        print(ex)
    finally:
        if spark is not None:
            print("Done!!")
            #spark.stop()





async def async_csv_write(task_name, dataframe, write_flag):
    def save_to_csv(df, file_path):
        try:
            df.to_csv(task_name)
        except Exception as e:
            print(f"Error while writing to CSV: {e}")

    if write_flag.lower() == "yes":
        try:
            df_to_csv = dataframe.toPandas()
            # Run the blocking operation in a separate thread
            loop = asyncio.get_running_loop()
            with ThreadPoolExecutor() as pool:
                await loop.run_in_executor(pool, save_to_csv, df_to_csv, task_name)
        except Exception as e:
            print(f"Error during CSV preparation: {e}")

# Example usage
# asyncio.run(async_csv_write("task1", dataframe, "yes"))


process_data()
