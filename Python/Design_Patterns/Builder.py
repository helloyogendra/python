### 1. **Define the Data Processing Builder Class**

# In this example, we'll build a `DataFrameBuilder` class that encapsulates various transformation steps, 
# such as filtering, joining, and aggregating.

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.functions import col



class DataFrameBuilder:
    def __init__(self, dataframe: DataFrame):
        self._dataframe = dataframe

    def filter_data(self, column_name: str, condition: str):
        """Filter rows based on a condition."""
        self._dataframe = self._dataframe.filter(col(column_name) == condition)
        return self  # Return self to allow chaining

    def join_data(self, other: DataFrame, join_column: str, join_type: str = "inner"):
        """Join with another DataFrame."""
        self._dataframe = self._dataframe.join(other, on=join_column, how=join_type)
        return self

    def select_columns(self, *columns):
        """Select specific columns."""
        self._dataframe = self._dataframe.select(*columns)
        return self

    def aggregate_data(self, group_by_column: str, agg_column: str, agg_func: str):
        """Aggregate data using functions like sum, avg, etc."""
        if agg_func == 'sum':
            self._dataframe = self._dataframe.groupBy(group_by_column).sum(agg_column)
        elif agg_func == 'avg':
            self._dataframe = self._dataframe.groupBy(group_by_column).avg(agg_column)
        # Additional aggregation functions as needed
        return self

    def build(self):
        """Return the fully constructed DataFrame."""
        return self._dataframe



# Using the Builder Pattern
# With the DataFrameBuilder, 
# you can create a transformation pipeline for your PySpark DataFrame by chaining the operations together. 
# This allows you to easily define the processing steps in a flexible, readable way.

    
# Initialize Spark session
spark = SparkSession.builder.appName("DataProcessingApp").getOrCreate()

# Sample data to create initial DataFrames
data1 = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
data2 = [("Alice", "HR"), ("Bob", "Engineering")]

# Create sample DataFrames
df1 = spark.createDataFrame(data1, ["name", "age"])
df2 = spark.createDataFrame(data2, ["name", "department"])

# Use the Builder to apply transformations
processed_df = (DataFrameBuilder(df1)
                .filter_data("age", "34")                       # Filter to get age 34
                .join_data(df2, "name")                         # Join with another DataFrame
                .select_columns("name", "age", "department")    # Select specific columns
                .aggregate_data("department", "age", "avg")     # Aggregate by department
                .build())                                       # Complete the build

# Show the final result
processed_df.show()
