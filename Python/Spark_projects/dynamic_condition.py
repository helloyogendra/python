import re
from functools import reduce

from pyspark.sql import Row, SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("dynamic_condition_demo").getOrCreate()

# Sample data: a small fruit stock table and a small fruit sales table
stock_df = spark.createDataFrame([
    Row(fruit="Mango", category="Fruit", color="Yellow", stockQty=120),
    Row(fruit="Banana", category="Fruit", color="Yellow", stockQty=300),
    Row(fruit="Apple", category="Fruit", color="Red", stockQty=80),
    Row(fruit="Carrot", category="Vegetable", color="Orange", stockQty=200),
])

sales_df = spark.createDataFrame([
    Row(fruit="Mango", region="North", channel="Store", qty=20, isReturned="N"),
    Row(fruit="Banana", region="South", channel="Online", qty=45, isReturned="N"),
    Row(fruit="Apple", region="North", channel="Online", qty=10, isReturned="Y"),
    Row(fruit="Carrot", region="East", channel="Store", qty=0, isReturned="N"),
])

dataframes = {
    "stock": stock_df,
    "sales": sales_df,
}

# A single string encodes filter conditions for multiple tables:
#   table.field=value|value   -> keep rows where field is one of the values
#   table.field<>value|value  -> keep rows where field is none of the values
# Conditions for the same table are combined with AND.
conditions_string = (
    "stock.category=Fruit|Vegetable;"
    "stock.fruit=Mango|Banana|Apple;"
    "stock.color<>Red;"
    "sales.channel<>Online;"
    "sales.qty<>0;"
    "sales.isReturned<>Y"
)

for ss in conditions_string.split(";"):
    print(ss)
    for s in ss.split("."):
        print(s)

condition_pattern = re.compile(r'(\w+)\.(\w+)(<>|=)([^;]+)')

# Combine all conditions for each table into a single filter expression
combined_conditions = {}

for condition in conditions_string.split(';'):
    match = condition_pattern.match(condition)
    if match:
        table_name, column_name, operator, values_str = match.groups()

        values = values_str.split('|')

        column_expression = (
            reduce(lambda x, y: x | y, [col(column_name) == value for value in values])
            if '|' in values_str
            else col(column_name) == values_str
        )

        if operator == '<>':
            column_expression = ~column_expression

        if table_name in combined_conditions:
            combined_conditions[table_name] &= column_expression
        else:
            combined_conditions[table_name] = column_expression

# Apply the combined conditions to the respective DataFrames
for table_name, condition in combined_conditions.items():
    if table_name in dataframes:
        dataframes[table_name] = dataframes[table_name].filter(condition)
        print(f"\nFiltered '{table_name}':")
        dataframes[table_name].show(truncate=False)
    else:
        print(f"DataFrame for table '{table_name}' not found.")

spark.stop()
