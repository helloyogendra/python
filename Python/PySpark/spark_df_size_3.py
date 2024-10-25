from pyspark.sql import SparkSession
import time
import subprocess


spark = SparkSession.builder.appName("spark_2") \
    .master('local[4]') \
    .config('spark.driver.memory', '4g') \
    .config('spark.executor.memory', '2g') \
    .config('spark.sql.shuffle.partitions', '4') \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

print("===============================================")
print("Starting now...")
print("===============================================")

file1 = 'test_data.csv'
file2 = 'test_data2.csv'

cmd = ['free', '-m']
with open("1.txt", 'w') as file:
    subprocess.call(cmd, stdout=file) 

csv_dataframe_1 = spark.read.csv(file1, header=True)
csv_dataframe_2 = spark.read.csv(file2, header=True)

csv_dataframe_2.createOrReplaceTempView("csv_table")

print(" --------------------- View Created---------------------------- ")

tmp_df = spark.sql("""Select * from csv_table""")
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
print("===============================================")

rdd_2 = csv_dataframe_2.rdd.collect()
rdd_1 = csv_dataframe_1.rdd.collect()

with open("4.txt", 'w') as file:
    subprocess.call(cmd, stdout=file) 



print('Session Stopped...')


with open("5.txt", 'w') as file:
    subprocess.call(cmd, stdout=file) 

time.sleep(600)
spark.stop()
