### 1. Define the Domain Model

# First, define the `Product` class 
# representing your domain model.

from abc import ABC, abstractmethod

from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Depends

class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.product_id}, 
            name='{self.name}', price={self.price})"


### 2. Define the Product DTO

# Next, create a DTO class to 
# define the structure of the product data 
# that will be transferred over the API.


class ProductDTO(BaseModel):
    product_id: int
    name: str
    price: float

    class Config:
        orm_mode = True  # Enables compatibility with ORM models


### 3. Define the Product Repository Interface

# Now, create an interface for the repository, 
# which will define methods for saving and loading products.


class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product):
        """Save a Product."""
        pass

    @abstractmethod
    def load(self, product_id: int) -> Product:
        """Load a Product by ID."""
        pass


### 4. Implement the In-Memory Product Repository

# Here, we’ll implement 
# an in-memory repository for demonstration purposes.


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products = {}

    def save(self, product: Product):
        """Save a Product in memory."""
        self.products[product.product_id] = product

    def load(self, product_id: int) -> Product:
        """Load a Product from memory by ID."""
        return self.products.get(product_id)


### 5. Define the Product Controller with DTO

# Now, create a controller that will handle incoming API requests 
# related to `Product` entities, using the DTO for data transfer.


app = FastAPI()

# Initialize the in-memory product repository
product_repository = InMemoryProductRepository()


@app.post("/products/", response_model=ProductDTO)
async def create_product(product_dto: ProductDTO):
    """Create a new product."""
    new_product = Product(product_id=product_dto.product_id, name=product_dto.name, price=product_dto.price)
    product_repository.save(new_product)
    return new_product  # Return the ProductDTO response


@app.get("/products/{product_id}", response_model=ProductDTO)
async def get_product(product_id: int):
    """Get a product by ID."""
    product = product_repository.load(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return ProductDTO(product_id=product.product_id, name=product.name, price=product.price)  



### 6. Running the FastAPI Application

# To run the FastAPI application, 
# save the code above in a file (e.g., `main.py`) 
# and run it with Uvicorn:

# bash
# uvicorn main:app --reload


# ### 7. Testing the API

# You can test the API using tools 
# like Postman or Curl. Here’s how you can test it:

# Create a Product- 
# POST request to -> http://127.0.0.1:8000/products/:

# json
# {
#     "product_id": 1,
#     "name": "Laptop",
#     "price": 1200.50
# }


# Get a Product-
# GET request to -> http://127.0.0.1:8000/products/1:

# You should receive the product details in the response.
