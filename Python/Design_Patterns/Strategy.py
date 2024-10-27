### 1. **Define the Strategy Interface**
# Create an abstract base class to define the interface for all filter strategies. 
# Each filter strategy will implement a `filter` method.


from abc import ABC, abstractmethod
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col


class FilterStrategy(ABC):
    @abstractmethod
    def filter(self, dataframe: DataFrame) -> DataFrame:
        """Apply a filtering strategy to the DataFrame."""
        pass


### 2. **Implement Concrete Strategies**
# Each concrete strategy class implements a specific 
# filtering approach by defining its own `filter` method.
#### Filter by Status Strategy


class FilterByStatus(FilterStrategy):
    def __init__(self, status: str):
        self.status = status

    def filter(self, dataframe: DataFrame) -> DataFrame:
        return dataframe.filter(col("status") == self.status)


#### Filter by Date Range Strategy

class FilterByDateRange(FilterStrategy):
    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date

    def filter(self, dataframe: DataFrame) -> DataFrame:
        return dataframe.filter((col("date") >= self.start_date) & (col("date") <= self.end_date))


#### Filter by Product Category Strategy

class FilterByProductCategory(FilterStrategy):
    def __init__(self, category: str):
        self.category = category

    def filter(self, dataframe: DataFrame) -> DataFrame:
        return dataframe.filter(col("product_category") == self.category)


### 3. **Context Class to Use the Strategy**
# The `DataFilter` class will act as the context for applying a strategy. 
# It holds a reference to a `FilterStrategy` and can switch strategies dynamically.

class DataFilter:
    def __init__(self, strategy: FilterStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: FilterStrategy):
        """Set a new filtering strategy at runtime."""
        self._strategy = strategy

    def apply_filter(self, dataframe: DataFrame) -> DataFrame:
        """Apply the current strategy's filter method on the DataFrame."""
        return self._strategy.filter(dataframe)


### 4. **Using the Strategy Pattern**
# Create a DataFrame and apply different filter strategies 
# to it using the `DataFilter` context class.


# Initialize Spark session
spark = SparkSession.builder.appName("DataProcessingApp").getOrCreate()

# Sample data to create a DataFrame
data = [("A101", "Completed", "2024-01-10", "Electronics"),
        ("A102", "Pending", "2024-01-15", "Home"),
        ("A103", "Completed", "2024-01-20", "Electronics"),
        ("A104", "Completed", "2024-01-25", "Furniture")]

# Create DataFrame
df = spark.createDataFrame(data, ["order_id", "status", "date", "product_category"])

# Instantiate a DataFilter context with a specific strategy
data_filter = DataFilter(strategy=FilterByStatus("Completed"))
filtered_df = data_filter.apply_filter(df)
print("Filtered by Status:")
filtered_df.show()

# Switch to a date range strategy
data_filter.set_strategy(FilterByDateRange("2024-01-10", "2024-01-20"))
filtered_df = data_filter.apply_filter(df)
print("Filtered by Date Range:")
filtered_df.show()

# Switch to a product category strategy
data_filter.set_strategy(FilterByProductCategory("Electronics"))
filtered_df = data_filter.apply_filter(df)
print("Filtered by Product Category:")
filtered_df.show()

