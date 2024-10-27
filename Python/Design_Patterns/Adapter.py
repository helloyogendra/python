### 1. **Define the Product Class**
# First, define the `Product` 
# class representing your domain model.

import json
import os
from abc import ABC, abstractmethod
from pyspark.sql import SparkSession

class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price})"


### 2. **Define the Common Interface**

# Next, create an interface for the product storage, 
# which will define methods for saving and loading products.


class ProductStorage(ABC):
    @abstractmethod
    def save(self, product: Product):
        """Save a Product."""
        pass

    @abstractmethod
    def load(self, product_id: int) -> Product:
        """Load a Product by ID."""
        pass


### 3. **Implement the PostgreSQL Adapter**

# Now, implement an adapter for PostgreSQL 
# that adapts the `ProductStorage` interface 
# to work with a PostgreSQL database.


class PostgresProductAdapter(ProductStorage):
    def __init__(self, spark: SparkSession, jdbc_url: str, db_properties: dict):
        self.spark = spark
        self.jdbc_url = jdbc_url
        self.db_properties = db_properties

    def save(self, product: Product):
        """Save a Product to PostgreSQL."""
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
        """Load a Product from PostgreSQL by ID."""
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


### 4. **Implement the JSON File Adapter**

# Next, create an adapter for saving and loading products to and from a JSON file.


class JsonFileProductAdapter(ProductStorage):
    def __init__(self, json_file: str):
        self.json_file = json_file

    def save(self, product: Product):
        """Save a Product to a JSON file."""
        if not os.path.exists(self.json_file):
            data = []
        else:
            with open(self.json_file, 'r') as file:
                data = json.load(file)

        data.append({
            "product_id": product.product_id,
            "name": product.name,
            "price": product.price
        })

        with open(self.json_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Product saved to JSON file: {product}")

    def load(self, product_id: int) -> Product:
        """Load a Product from a JSON file by ID."""
        if not os.path.exists(self.json_file):
            return None

        with open(self.json_file, 'r') as file:
            data = json.load(file)

        for item in data:
            if item['product_id'] == product_id:
                return Product(item['product_id'], item['name'], item['price'])

        return None


### 5. **Using the Adapters in Your Application**

# Finally, demonstrate how to use the adapters 
# to save and load products using both PostgreSQL and JSON file storage.


# Set up the Spark session and database properties for PostgreSQL
spark = SparkSession.builder.appName("DataProcessingApp").getOrCreate()
jdbc_url = "jdbc:postgresql://localhost:5432/mydb"
db_properties = {
    "user": "myuser",
    "password": "mypassword",
    "driver": "org.postgresql.Driver"
}

# Create the PostgreSQL adapter instance
postgres_adapter = PostgresProductAdapter(spark, jdbc_url, db_properties)

# Create the JSON file adapter instance
json_adapter = JsonFileProductAdapter("products.json")

# Example product
new_product = Product(product_id=1, name="Laptop", price=1200.50)

# Save the product using PostgreSQL
postgres_adapter.save(new_product)

# Load the product by ID from PostgreSQL
loaded_product_postgres = postgres_adapter.load(1)
print("Loaded Product from PostgreSQL:", loaded_product_postgres)

# Save the product using JSON file storage
json_adapter.save(new_product)

# Load the product by ID from JSON file
loaded_product_json = json_adapter.load(1)
print("Loaded Product from JSON file:", loaded_product_json)

