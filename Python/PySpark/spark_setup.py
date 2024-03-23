# download and setup
#
# wget https://dlcdn.apache.org/spark/spark-3.5.0/spark-3.5.0-bin-hadoop3.tgz
# tar xvf spark-3.5.0-bin-hadoop3.tgz
# sudo mv spark-3.5.0-bin-hadoop3 /opt/spark
# export SPARK_HOME=/opt/spark
# export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
# source ~/.bashrc

# test the setup
#
# spark-shell
# pyspark
# spark-submit
# touch spark_demo_1.py
# vi spark_demo_1.py
# python3 spark_demo_1.py
# pyspark spark_demo_1.py

# run your code in pyspark
#
# spark-submit spark_demo_1.py
# mkdir project_spark
# cd project
# cd project_spark
# spark-submit spark_demo_1.py

from pyspark.sql import SparkSession
from pyspark import SparkContext


sc = SparkContext.getOrCreate()
conf = sc.getConf()

conf.set("spark.driver.memory", "2g")
conf.set("spark.executor.memory", "4g")

driver_memory =conf.get("spark.driver.memory")
ex_memory = conf.get("spark.executor.memory")

spark = SparkSession.builder.appName("app").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

file_path = "/home/hello/NIFTY50_all.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)