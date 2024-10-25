from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, TimestampType


def get_color_codes():
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    YELLOW = "\033[1;33m"
    RESET = "\033[0m"

    return RED, GREEN, BLUE, YELLOW, RESET



def create_dataframe():

    spark = SparkSession.builder.appName("app").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    data = [
        (1, "2023-10-27 11:05:24", 10),
        (1, "2023-10-27 11:10:24", 15),
        (1, "2023-10-27 11:15:24", 20),
        (2, "2023-10-27 11:20:24", 25),
        (2, "2023-10-27 11:25:24", 30),
        (2, "2023-10-27 11:35:24", 50),
        (3, "2023-10-27 11:40:24", 60),
        (3, "2023-10-27 11:45:24", 20),
        (1, "2023-10-27 11:50:24", 25),
        (1, "2023-10-27 11:55:24", 30),
        (2, "2023-10-27 12:00:24", 30),
        (2, "2023-10-27 12:10:24", 40),
    ]

    columns = ["id","start", "value"]

    schema = StructType([
        StructField("id", IntegerType()),
        StructField("start", TimestampType()),
        StructField("value", IntegerType())
    ])

    df = spark.createDataFrame(data, columns)

    _, G, _, _, RS = get_color_codes()

    print(f"{G}Column names are: {df.columns}{RS}")
    print(f"{G}Column Data-type : {df.dtypes}{RS}")

    time_format = "yyyy-MM-dd HH:mm:ss"

    df = df.withColumn("start", F.to_timestamp(df["start"], time_format))
    df = df.withColumn("end", F.col("start") + F.expr ('INTERVAL 15 MINUTES'))
    df = df.withColumn("start_long", F.col("start").cast("long"))
    df = df.orderBy("start")

    return df


def create_small_dataframe():

    spark = SparkSession.builder.appName("app").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    data = [
        (1, "2023-10-27 11:05:24", 10),
        (1, "2023-10-27 11:10:24", 15),
        (1, "2023-10-27 11:15:24", 20),
        (2, "2023-10-27 11:20:24", 25),
        (2, "2023-10-27 11:25:24", 30),
    ]

    columns = ["id","start", "value"]

    df = spark.createDataFrame(data, columns)

    _, G, _, _, RS = get_color_codes()

    print(f"{G}Column names are: {df.columns}{RS}")
    print(f"{G}Column Data-type : {df.dtypes}{RS}")

    time_format = "yyyy-MM-dd HH:mm:ss"

    df = df.withColumn("start", F.to_timestamp(df["start"], time_format))
    df = df.withColumn("end", F.col("start") + F.expr ('INTERVAL 15 MINUTES'))
    df = df.withColumn("start_long", F.col("start").cast("long"))
    df = df.orderBy("start")

    return df





def create_order_dataframe():

    spark = SparkSession.builder.appName("app").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    data = [
        ("a", 1, "2023-10-27 11:05:24", 10),
        ("a", 4, "2023-10-27 11:10:24", 15),
        ("a", 3, "2023-10-27 11:15:24", 20),
        ("a", 2, "2023-10-27 11:20:24", 25),  #2

        ("b", 2, "2023-10-27 11:25:24", 30),
        ("b", 3, "2023-10-27 11:35:24", 50),
        ("b", 4, "2023-10-27 11:40:24", 60),
        ("b", 1, "2023-10-27 11:45:24", 20),  #1

        ("c", 1, "2023-10-27 11:50:24", 25),
        ("c", 3, "2023-10-27 11:55:24", 30),
        ("c", 4, "2023-10-27 12:00:24", 30),
        ("c", 2, "2023-10-27 12:10:24", 40),  #2
    ]

    columns = ["sym", "id","start", "value"]

    schema = StructType([
        StructField("id", IntegerType()),
        StructField("start", TimestampType()),
        StructField("value", IntegerType())
    ])

    df = spark.createDataFrame(data, columns)

    _, G, _, _, RS = get_color_codes()

    print(f"{G}Column names are: {df.columns}{RS}")
    print(f"{G}Column Data-type : {df.dtypes}{RS}")

    time_format = "yyyy-MM-dd HH:mm:ss"

    df = df.withColumn("start", F.to_timestamp(df["start"], time_format))
    df = df.withColumn("end", F.col("start") + F.expr ('INTERVAL 15 MINUTES'))
    df = df.withColumn("start_long", F.col("start").cast("long"))
    df = df.orderBy("start")

    return df




def create_grouped_dataframe():

    spark = SparkSession.builder.appName("app").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    data = [
        (1, 1, 3),
        (1, 2, 4),
        (1, 3, 2),
        (1, 4, 1),

        (2, 1, 1),
        (2, 2, 3),
        (2, 3, 2),

        (3, 1, 1),
        (3, 2, 3),
        (3, 3, 2),
        (3, 3, 4)
    ]

    columns = ["id", "times","sym"]

    df = spark.createDataFrame(data, columns)

    _, G, _, _, RS = get_color_codes()

    print(f"{G}Column names are: {df.columns}{RS}")
    print(f"{G}Column Data-type : {df.dtypes}{RS}")

    df = df.orderBy("id")

    return df


