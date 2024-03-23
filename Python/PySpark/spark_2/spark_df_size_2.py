from pyspark.sql import SparkSession
import time
import subprocess
import sys

start_time = time.perf_counter()
args = sys.argv[1:]

# Multiple Spark Session - submit single job to each new session - additional parameter also required

print("######################## Get sys args ################################ \n ")

print(type(args[0]), " = ", (args[0]))
print(type(args[1]), " = ", (args[1]))
print(type(args[1]), " = ", (args[2]))

print("######################## Split sys args ################################ \n ")

print(str(args[0]).split(','))
print(str(args[1]).split(','))

print("######################## Dict sys args ################################ \n ")

print(f"{dict(zip(str(args[0]).split(','), str(args[1]).split(',')))}")

print("######################## Done sys args ################################ \n ")

#driver=4g, executor=2g

session_name = f"spark_session_{args[2]}"

spark = SparkSession.builder.appName(session_name) \
    .master('local[1]') \
    .config('spark.driver.memory', '2g') \
    .config('spark.executor.memory', '1g') \
    .config('spark.sql.shuffle.partitions', '4') \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("===============================================")
print("Starting now...")
print("===============================================")

file1 = 'test_data.csv'
file2 = 'test_data3.csv'

cmd = ['free', '-m']
with open("1.txt", 'w') as file:
    subprocess.call(cmd, stdout=file) 

csv_dataframe_1 = spark.read.csv(file1, header=True)
csv_dataframe_2 = spark.read.csv(file2, header=True)

csv_dataframe_2.createOrReplaceTempView("csv_table")

print(" --------------------- View Created---------------------------- ")

tmp_df = spark.sql("""Select * from csv_table where Year > 2018 and Area in (1, 2, 3, 4, 5, 6, 7, 8, 9) and (name like 'ABC%DEF' or name like '_QRSTUV')""")
print("tmp df done ====================================================")
print(tmp_df.count())
tmp_df.show(truncate=False)

with open("2.txt", 'w') as file:
    subprocess.call(cmd, stdout=file) 

rdd_1 = csv_dataframe_1.rdd
rdd_1.persist()

csv_dataframe_1.cache()
csv_dataframe_2.cache()

with open("3.txt", 'w') as file:
    subprocess.call(cmd, stdout=file)  

print("===============================================")
print("First Count is : ", csv_dataframe_1.count())
print("Second Count is : ", csv_dataframe_2.count())

filters = "(name like 'ABC%DEF')"
csv_dataframe_2.filter(filters).show()

print("================= To Pandas -> CSV ==============================")

pd1 = csv_dataframe_1.toPandas()
pd1.to_csv(session_name + "_1.csv")

pd2 = csv_dataframe_2.toPandas()
pd2.to_csv(session_name + "_2.csv")

end_time = time.perf_counter()
print(f"Multi Spark Session : run time is {end_time - start_time} seconds")

print('Waiting for 60 seconds to stop the session...')
time.sleep(60)
spark.stop()
print('Session Stopped...')
