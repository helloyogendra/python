# Factory Design Patterns:
# 
# Version - 1

from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Factory
class AnimalFactory:
    @staticmethod
    def get_animal(animal_type: str) -> Animal:
        if animal_type == "Dog":
            return Dog()
        elif animal_type == "Cat":
            return Cat()
        else:
            raise ValueError("Unknown animal type")


# Client code
if __name__ == "__main__":

    animal1 = AnimalFactory.get_animal("Dog")
    print(animal1.speak())                          # Output: Woof!

    animal2 = AnimalFactory.get_animal("Cat")
    print(animal2.speak())                          # Output: Meow!



# 
# Version - 2

from enum import Enum
from abc import ABC, abstractmethod
from typing import Annotated, TypeAlias, NewType


class Shape_Keys(Enum):
    CIRCLE = "circle"
    SQUARE = "square"
    RECTANGLE = "rectangle"


# Product interface
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

# Concrete Products
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

# Factory
class ShapeFactory:
    @staticmethod
    def get_shape(shape_type: Shape_Keys) -> Shape:
        if shape_type == Shape_Keys.CIRCLE:
            return Circle()
        elif shape_type == Shape_Keys.SQUARE:
            return Square()
        else:
            raise ValueError("Unknown shape type")


# Client code
if __name__ == "__main__":

    Fact: TypeAlias = ShapeFactory

    shape1 = Fact.get_shape(Shape_Keys.CIRCLE)
    print(shape1.draw())                            # Output: Drawing a Circle

    shape2 = Fact.get_shape(Shape_Keys.SQUARE)
    print(shape2.draw())                            # Output: Drawing a Square




# 
# CSV File Factory
# 

# Let’s say you have two types of CSV files:

# Sales Data: Requires filtering, aggregation, and formatting.
# Inventory Data: Requires joining with another dataset and performing some calculations

from abc import ABC, abstractmethod
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col

class DataProcessor(ABC):
    @abstractmethod
    def process(self, dataframe: DataFrame) -> DataFrame:
        """Process the DataFrame based on specific logic."""
        pass


### 2. **Define Specific Processing Classes**
# Each class below defines a different type of data processing, 
# implementing the `process` method as per the specific business logic for that data type.

#### Sales Data Processor

class SalesDataProcessor(DataProcessor):
    def process(self, dataframe: DataFrame) -> DataFrame:
        # Filter for completed sales and calculate total revenue
        df = dataframe.filter(col("status") == "Completed")
        df = df.groupBy("product_id").sum("revenue")
        return df


#### Inventory Data Processor


class InventoryDataProcessor(DataProcessor):
    def process(self, dataframe: DataFrame) -> DataFrame:
        # Example: Perform a join with a products DataFrame to add product details
        products_df = dataframe.sparkSession.createDataFrame(
            [("A101", "Gadget"), ("B202", "Widget")], ["product_id", "product_name"]
        )
        df = dataframe.join(products_df, on="product_id", how="left")
        df = df.withColumn("stock_value", col("quantity") * col("price_per_unit"))
        return df


### 3. **Implement the Factory Class**
# The factory, `DataProcessorFactory`, 
# will determine the type of processor to instantiate based on a provided identifier, 
# such as the file type.


class DataProcessorFactory:
    @staticmethod
    def get_processor(file_type: str) -> DataProcessor:
        """Factory method to get the appropriate DataProcessor."""
        if file_type == "sales":
            return SalesDataProcessor()
        elif file_type == "inventory":
            return InventoryDataProcessor()
        else:
            raise ValueError(f"Unknown file type: {file_type}")


### 4. **Using the Factory to Process Data**
# Now, you can use the `DataProcessorFactory` 
# to dynamically create and run the appropriate data processing pipeline.


# Initialize Spark session
spark = SparkSession.builder.appName("DataProcessingApp").getOrCreate()

# Sample data for Sales and Inventory
sales_data = [("A101", "Completed", 500.0), ("A102", "Pending", 300.0)]
inventory_data = [("A101", 100, 10.0), ("B202", 200, 15.0)]

# Create DataFrames for Sales and Inventory
sales_df = spark.createDataFrame(sales_data, ["product_id", "status", "revenue"])
inventory_df = spark.createDataFrame(inventory_data, ["product_id", "quantity", "price_per_unit"])

# Processing Sales Data
processor = DataProcessorFactory.get_processor("sales")
processed_sales_df = processor.process(sales_df)
processed_sales_df.show()

# Processing Inventory Data
processor = DataProcessorFactory.get_processor("inventory")
processed_inventory_df = processor.process(inventory_df)
processed_inventory_df.show()

