# 1. Define the Event Class
# First, create an event class to represent user registration events.

from fastapi import FastAPI, HTTPException

class UserRegisteredEvent:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


# 2. Define the Event Bus
# Now, we’ll create an event bus that manages 
# the subscription and publication of events.

class EventBus:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type: str, subscriber):
        """Subscribe a listener to an event type."""

        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)

    def publish(self, event):
        """Publish an event to all subscribed listeners."""
        
        event_type = type(event).__name__
        for subscriber in self.subscribers.get(event_type, []):
            subscriber.handle(event)


# 3. Define Event Handlers (Listeners)
# Now, implement event handlers 
# that will respond to user registration events.


class WelcomeEmailHandler:
    def handle(self, event: UserRegisteredEvent):
        """Send a welcome email to the user."""

        print(f"Sending welcome email to {event.email}")

class RegistrationLogger:
    def handle(self, event: UserRegisteredEvent):
        """Log the registration event."""

        print(f"User registered: {event.username} with email {event.email}")


# 4. Define the FastAPI Application
# Now we can integrate everything into a FastAPI application.


app = FastAPI()
event_bus = EventBus()

# Create event handlers
welcome_email_handler = WelcomeEmailHandler()
registration_logger = RegistrationLogger()

# Subscribe handlers to the UserRegisteredEvent
event_bus.subscribe(UserRegisteredEvent.__name__, welcome_email_handler)
event_bus.subscribe(UserRegisteredEvent.__name__, registration_logger)

@app.post("/register/")
async def register_user(username: str, email: str):
    """User registration endpoint."""
    # Simulate user registration logic here

    if not username or not email:
        raise HTTPException(status_code=400, 
                            detail="Username and email are required.")

    # Create a UserRegisteredEvent
    event = UserRegisteredEvent(username=username, email=email)

    # Publish the event
    event_bus.publish(event)

    return {"message": "User registered successfully", 
            "username": username, "email": email}


# 5. Running the FastAPI Application
# To run the FastAPI application, save the code and run it with Uvicorn:
# bash
# uvicorn main:app --reload

# 6. Testing the API
# You can test the API using tools like Postman or Curl. 
# Here’s how you can test it:
# Register User Request-
# POST request to -> http://127.0.0.1:8000/register/:

# json
# {
#     "username": "JaneDoe",
#     "email": "janedoe@example.com"
# }

