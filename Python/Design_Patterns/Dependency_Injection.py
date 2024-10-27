### 1. Define the Product Class

# First, define the `Product` class 
# representing your domain model.


class Product:
    def __init__(self, product_id: int, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(id={self.product_id}, name='{self.name}', price={self.price})"


### 2. Define the Product Repository Interface

# Next, create an interface for the repository, 
# which will define methods for saving and loading products.


from abc import ABC, abstractmethod

class ProductRepository(ABC):
    @abstractmethod
    def save(self, product: Product):
        """Save a Product."""
        pass

    @abstractmethod
    def load(self, product_id: int) -> Product:
        """Load a Product by ID."""
        pass


### 3. Implement the In-Memory Product Repository

# We’ll implement an in-memory repository for demonstration purposes.


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products = {}

    def save(self, product: Product):
        """Save a Product in memory."""
        self.products[product.product_id] = product

    def load(self, product_id: int) -> Product:
        """Load a Product from memory by ID."""
        return self.products.get(product_id)


### 4. Define the Product Controller

# Next, create a controller that will handle 
# incoming API requests related to `Product` entities.


from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()

class ProductModel(BaseModel):
    product_id: int
    name: str
    price: float

# Initialize the in-memory product repository
product_repository = InMemoryProductRepository()

@app.post("/products/")
async def create_product(product: ProductModel, repo: ProductRepository = Depends(lambda: product_repository)):
    """Create a new product."""
    new_product = Product(product_id=product.product_id, name=product.name, price=product.price)
    repo.save(new_product)
    return {"message": "Product created successfully", "product": new_product}

@app.get("/products/{product_id}")
async def get_product(product_id: int, repo: ProductRepository = Depends(lambda: product_repository)):
    """Get a product by ID."""
    product = repo.load(product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


### 5. **Running the FastAPI Application**

# To run the FastAPI application, 
# save the code above in a file (e.g., `main.py`) and run it with Uvicorn:

# bash
# uvicorn main:app --reload


# ### 6. Testing the API

# You can test the API using tools like Postman or Curl. 
# Here’s how you can test it:

# Create a Product (POST request to `http://127.0.0.1:8000/products/`):

# json
# {
#     "product_id": 1,
#     "name": "Laptop",
#     "price": 1200.50
# }


# Get a Product (GET request to `http://127.0.0.1:8000/products/1`):

# You should receive the product details in the response.
