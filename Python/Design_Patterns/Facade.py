### 1. Define Subsystem Components
# First, we'll define the various components 
# that will be part of the shopping cart subsystem:

from fastapi import FastAPI

class Inventory:
    def check_stock(self, product_id: int) -> bool:
        """Check if the product is in stock."""

        # For demonstration purposes, 
        # we'll assume products with ID 1 to 3 are in stock

        return product_id in {1, 2, 3}

    def reserve_product(self, product_id: int):
        
        """Reserve the product in the inventory."""
        print(f"Product {product_id} reserved in inventory.")

class PaymentProcessor:
    def process_payment(self, amount: float):

        """Process the payment."""
        print(f"Payment of ${amount:.2f} processed successfully.")

class NotificationService:
    def send_notification(self, message: str):

        """Send notification to the user."""
        print(f"Notification sent: {message}")


### 2. Define the Facade Class
# Next, create a `ShoppingCart` facade 
# that will interact with these subsystem components.


class ShoppingCartFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment_processor = PaymentProcessor()
        self.notification_service = NotificationService()

    def checkout(self, product_id: int, quantity: int, price: float):
        """Handle the checkout process."""

        if self.inventory.check_stock(product_id):
            self.inventory.reserve_product(product_id)
            total_amount = quantity * price
            self.payment_processor.process_payment(total_amount)
            self.notification_service.send_notification(
                f"Order placed for product {product_id}. Total: ${total_amount:.2f}")

            return {"message": "Checkout successful", "total_amount": total_amount}
        else:
            return {"message": "Product is out of stock."}


### 3. Define the FastAPI Application
# Now, we can integrate everything into a FastAPI application.


app = FastAPI()
shopping_cart = ShoppingCartFacade()

@app.post("/checkout/")
async def checkout(product_id: int, quantity: int, price: float):
    """Checkout endpoint."""
    result = shopping_cart.checkout(product_id, quantity, price)
    return result


### 4. Running the FastAPI Application
# To run the FastAPI application, 
# save the code and run it with Uvicorn:
# bash
# uvicorn main:app --reload

# ### 5. Testing the API
# You can test the API using tools like Postman or Curl. 
# Here’s how you can test it:
# Checkout Request
# POST request to `http://127.0.0.1:8000/checkout/:

# json
# {
#     "product_id": 1,
#     "quantity": 2,
#     "price": 150.00
# }