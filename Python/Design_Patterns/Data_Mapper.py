### 1. **Define the Product Class
# First, define a simple `Product` class 
# that represents your domain model.


import json
from abc import ABC, abstractmethod
from pyspark.sql import SparkSession, DataFrame


class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price})"


### 2. **Define the Data Mapper Interface**
# Next, create an interface for the data mapper. 
# This will define methods for saving and loading `Product` objects.



class ProductMapper(ABC):
    @abstractmethod
    def save(self, product: Product):
        """Save a Product to the database."""
        pass

    @abstractmethod
    def load(self, product_id: int) -> Product:
        """Load a Product from the database by ID."""
        pass


### 3. **Implement the PostgreSQL Data Mapper**

# Now, implement the `ProductMapper` 
# interface for PostgreSQL using a class. 
# This class will handle the connection to the database 
# and implement the logic to save and load products.



class PostgresProductMapper(ProductMapper):
    def __init__(self, spark: SparkSession, jdbc_url: str, db_properties: dict):
        self.spark = spark
        self.jdbc_url = jdbc_url
        self.db_properties = db_properties

    def save(self, product: Product):
        """Save a Product to the database."""
        # Convert Product to DataFrame
        product_data = [(product.product_id, product.name, product.price)]
        df = self.spark.createDataFrame(product_data, ["product_id", "name", "price"])

        # Save DataFrame to PostgreSQL
        df.write.jdbc(
            url=self.jdbc_url,
            table="products",
            mode="append",
            properties=self.db_properties
        )
        print(f"Product saved to PostgreSQL: {product}")

    def load(self, product_id: int) -> Product:
        """Load a Product from the database by ID."""
        df = self.spark.read.jdbc(
            url=self.jdbc_url,
            table="products",
            properties=self.db_properties
        )

        product_row = df.filter(df.product_id == product_id).collect()
        if product_row:
            return Product(product_row[0].product_id, product_row[0].name, product_row[0].price)
        else:
            return None


### 4. **Using the Data Mapper in Your Application**

# Finally, let’s see how to use the `PostgresProductMapper` 
# to save and load products.


# Set up the Spark session and database properties

spark = SparkSession.builder.appName("DataProcessingApp").getOrCreate()
jdbc_url = "jdbc:postgresql://localhost:5432/mydb"
db_properties = {
    "user": "myuser",
    "password": "mypassword",
    "driver": "org.postgresql.Driver"
}

# Create the product mapper instance
product_mapper = PostgresProductMapper(spark, jdbc_url, db_properties)

# Example product
new_product = Product(product_id=1, name="Laptop", price=1200.50)

# Save the product
product_mapper.save(new_product)

# Load the product by ID
loaded_product = product_mapper.load(1)
print("Loaded Product:", loaded_product)

