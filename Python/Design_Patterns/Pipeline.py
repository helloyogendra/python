# 1. Define the Pipeline Step Interface
# First, define an interface for pipeline steps 
# that will be used in the processing pipeline.

from abc import ABC, abstractmethod
from fastapi import FastAPI, HTTPException

class PipelineStep(ABC):
    @abstractmethod
    def execute(self, data: dict) -> dict:
        """Process the input data and return the modified data."""
        pass


# 2. Define Concrete Pipeline Steps
# Now define concrete pipeline steps for validation, 
# sanitization, and saving the user data.


class ValidationStep(PipelineStep):
    def execute(self, data: dict) -> dict:
        """Validate the user data."""
        if "username" not in data or "email" not in data:
            raise ValueError("Missing username or email.")
        return data

class SanitizationStep(PipelineStep):
    def execute(self, data: dict) -> dict:
        """Sanitize the user data."""
        data["username"] = data["username"].strip()
        data["email"] = data["email"].strip().lower()
        return data

class SaveToDatabaseStep(PipelineStep):
    def execute(self, data: dict) -> dict:
        """Simulate saving user data to a database."""
        # In a real application, you would perform the database operation here.

        print(f"User {data['username']} saved to database.")
        return data


# 3. Define the Pipeline Class
# Now, create a `Pipeline` class 
# that will manage the execution of the pipeline steps.


class Pipeline:
    def __init__(self):
        self.steps = []

    def add_step(self, step: PipelineStep):
        """Add a step to the pipeline."""
        self.steps.append(step)

    def execute(self, data: dict) -> dict:
        """Execute the pipeline steps in order."""
        for step in self.steps:
            data = step.execute(data)
        return data


# 4. Define the FastAPI Application
# Now we can integrate everything into a FastAPI application.




app = FastAPI()
pipeline = Pipeline()

# Add steps to the pipeline
pipeline.add_step(ValidationStep())
pipeline.add_step(SanitizationStep())
pipeline.add_step(SaveToDatabaseStep())

@app.post("/register/")
async def register_user(username: str, email: str):
    """User registration endpoint."""
    user_data = {"username": username, "email": email}
    
    try:
        processed_data = pipeline.execute(user_data)
        return {"message": "User registered successfully", "data": processed_data}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# 5. Running the FastAPI Application
# To run the FastAPI application and run it with Uvicorn:
# bash
# uvicorn main:app --reload

# 6. Testing the API
# You can test the API using tools like Postman or Curl. 
# Here’s how you can test it:
# Register User Request-
# POST request to -> http://127.0.0.1:8000/register/:

# json
# {
#     "username": "  JohnDoe ",
#     "email": "  JohnDoe@Example.com  "
# }

