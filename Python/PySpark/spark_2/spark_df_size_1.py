from pyspark.sql import SparkSession
import time
import subprocess
import sys
import os
from threading import Thread
from multiprocessing import Process

def json_func(row):
    from datetime import datetime
    output_dir = "/home/hello/project_spark/test_results"
    file_name = os.path.join(output_dir, f'{str(datetime.now()).replace(":", "_")}.json')
    row.to_json(file_name)

def panda(df):
    import time
    a = time.perf_counter()
    if df:
        pd2 = df.toPandas()

        for index, row in pd2.iterrows():
            #json_func(row)
            thread = Thread(target=json_func, args=(row,))
            thread.start()
            print(f"{index+1} file exported")
        

        #pd2.to_csv("/home/hello/project_spark/test_results/spark_2_df.csv")
        #print("file exported")
        #print(time.perf_counter()-a)
    else:
        print("dataframe is None in panda function ")
    print(time.perf_counter()-a)

start_time = time.perf_counter()

# args = sys.argv[1:]

# Single Spark Session - submit multiple jobs

print("######################## Get sys args ################################ \n ")
print(start_time)

# print(type(args[0]), " = ", (args[0]))
# print(type(args[1]), " = ", (args[1]))
# print(type(args[1]), " = ", (args[2]))

print("######################## Split sys args ################################ \n ")

# print(str(args[0]).split(','))
# print(str(args[1]).split(','))

print("######################## Dict sys args ################################ \n ")

# print(f"{dict(zip(str(args[0]).split(','), str(args[1]).split(',')))}")

print("######################## Done sys args ################################ \n ")

#driver=4g, executor=2g

# spark = SparkSession.builder.appName("spark_1") \
#     .master('local[1]') \
#     .config('spark.driver.memory', '4g') \
#     .config('spark.executor.memory', '1g') \
#     .config('spark.sql.shuffle.partitions', '4') \
#     .getOrCreate()

spark = SparkSession.builder.appName("spark_1").master('local[1]').getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("===============================================")
print("Starting now...")
print("===============================================")

# file1 = '/home/hello/project_spark/test_data/big_data.csv'
file2 = '/home/hello/project_spark/test_data/bigger_data.csv'

cmd = ['free', '-m']
with open("/home/hello/project_spark/logs/1.txt", 'w') as file:
    subprocess.call(cmd, stdout=file) 

# csv_dataframe_1 = spark.read.csv(file1, header=True)
csv_dataframe_2 = spark.read.csv(file2, header=True)
# csv_dataframe_2.createOrReplaceTempView("csv_table")

print(" --------------------- View Created---------------------------- ")

# query = """Select * from csv_table where Year > 2018 and Area in (1, 2, 3, 4, 5, 6, 7, 8, 9) and (name like 'ABC%DEF' or name like '_QRSTUV')"""
# tmp_df = spark.sql(query)

filters = "Year > 2018 and Area in (1, 2, 3, 4, 5, 6, 7, 8, 9) and (name like 'ABC%DEF' or name like '_QRSTUV')"
tmp_df = csv_dataframe_2.filter(filters)

print("====================================================")
print("Filtered data count is : ", tmp_df.count())
tmp_df.show(truncate=False)
# tmp_df.persist()

with open("/home/hello/project_spark/logs/2.txt", 'w') as file:
    subprocess.call(cmd, stdout=file) 

# rdd_1 = csv_dataframe_1.rdd
# rdd_1.persist()

# csv_dataframe_1.cache()
# csv_dataframe_2.persist()

with open("/home/hello/project_spark/logs/3.txt", 'w') as file:
    subprocess.call(cmd, stdout=file)  

print("===============================================")
# print("First Count is : ", csv_dataframe_1.count())
# print("Second Count is : ", csv_dataframe_2.count())



print("================= Two CSV Files : Size = 300 MB and 1500 MB ==============================")
print("================= To Pandas -> CSV =======================================================")

# 205 seconds with pandas -> csv : Single file where size = 1500 MB : double filters
# 204 seconds with spark -> csv : Single file where size = 1500 MB : double filters

# 52 seconds with pandas -> csv : Single file where size = 1500 MB : single SQL/View filter
# 56 seconds with spark -> csv : Single file where size = 1500 MB : single SQL/View filter

# 48 seconds with pandas -> csv : Single file where size = 1500 MB : single dataframe filter
# 48 seconds with spark -> csv : Single file where size = 1500 MB : single dataframe filter

# 47 seconds with pandas -> csv : Single file where size = 1500 MB : single dataframe filter [used threading] [single instance]
# 47 seconds with pandas -> csv : Single file where size = 1500 MB : single dataframe filter [used threading - joined] [single instance]

# 126 seconds with pandas -> csv : Single file where size = 1500 MB : single dataframe filter [used dual stage threading] [six instance multiprocessing]

# 123 seconds with pandas -> csv : Single file where size = 1500 MB : single dataframe filter [six instance multiprocessing, no threading]

# 118 seconds with pandas -> csv : Single file where size = 1500 MB : single dataframe filter [used single stage threading] [six instance multiprocessing]
# Outer Function         - Inner Function Thread. [combined with above line]

try:
    # pd1 = csv_dataframe_1.toPandas()
    # pd1.to_csv("/home/hello/project_spark/test_results/spark_1_df.csv")# + str(args[2]) + "_df1.csv")

    # above two lines or below one line
    #csv_dataframe_1.write.mode("overwrite").csv('/home/hello/project_spark/test_results/')

    # pd2 = tmp_df.toPandas()
    # pd2.to_csv("/home/hello/project_spark/test_results/spark_2_df.csv")# + str(args[2]) + "_df2.csv")

    # thread = Thread(target=panda, args=(tmp_df,))
    # thread.start()
    # thread.join()
    panda(tmp_df)
    # thread = Thread(target=panda, args=(tmp_df,))
    # thread.start()
    # tmp_df.write.mode("overwrite").csv('/home/hello/project_spark/test_results/')
except:
    print('Session Crashed and Stopped...')
    # tmp_df.unpersist()
    # csv_dataframe_2.unpersist()
    spark.stop()

# tmp_df.unpersist()
# csv_dataframe_2.unpersist()

with open("/home/hello/project_spark/logs/4.txt", 'w') as file:
    subprocess.call(cmd, stdout=file) 

end_time = time.perf_counter()
print(f"Single Spark Session : run time is {end_time - start_time} seconds")

# time.sleep(60)
if spark:
    print('Session Stopped Normally...')


# Approach
# Outer Function Thread  - Inner Function.
# Outer Function Thread  - Inner Function Thread.
# Outer Function         - Inner Function Thread. [*]
# Outer Function Process - Inner Function Thread.
# Outer Function Thread  - Inner Function Process.





