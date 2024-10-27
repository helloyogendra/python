### 1. Define the Observer Interface
# First, define an interface for the observers that will be notified of changes.

from abc import ABC, abstractmethod
from fastapi import FastAPI


class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        """Receive update from the subject."""
        pass


### 2. Define the Subject Class
# Next, create a `Subject` class that manages observers and notifies them when a product is created.


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        """Attach an observer to the subject."""
        self._observers.append(observer)

    def detach(self, observer: Observer):
        """Detach an observer from the subject."""
        self._observers.remove(observer)

    def notify(self, message: str):
        """Notify all observers of a change."""
        for observer in self._observers:
            observer.update(message)


### 3. Define Concrete Observers
# Implement concrete observer classes that will react to notifications.

class EmailNotifier(Observer):
    def update(self, message: str):
        print(f"Email Notification: {message}")

class LoggingObserver(Observer):
    def update(self, message: str):
        print(f"Log Entry: {message}")


### 4. Define the Product Service Using Observer Pattern
# Now, create a service that manages products and notifies observers when a product is created.

class ProductService(Subject):
    def __init__(self):
        super().__init__()

    def create_product(self, product_id: int, name: str, price: float):
        """Create a new product and notify observers."""
        # Simulating product creation logic
        message = f"Product created: ID={product_id}, Name={name}, Price=${price}"
        self.notify(message)  # Notify all observers


### 5. Define the FastAPI Application
# Now we can integrate everything into a FastAPI application.

app = FastAPI()
product_service = ProductService()

# Attach observers to the product service
product_service.attach(EmailNotifier())
product_service.attach(LoggingObserver())

@app.post("/products/")
async def create_product(product_id: int, name: str, price: float):
    """Create a new product."""
    product_service.create_product(product_id, name, price)
    return {"message": "Product created successfully", "product_id": product_id, "name": name, "price": price}


### 6. Running the FastAPI Application
# To run the FastAPI application, save the code above in a file (e.g., `main.py`) and run it with Uvicorn:
# bash
# uvicorn main:app --reload


### 7. Testing the API
# You can test the API using tools like Postman or Curl. Here’s how you can test it:

# Create a Product-
# POST request to -> http://127.0.0.1:8000/products/:

# json
# {
#     "product_id": 1,
#     "name": "Laptop",
#     "price": 1200.50
# }
# 

