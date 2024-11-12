# Single Responsibility Principle (SRP)
# SRP states that a class should have only one reason to change, meaning it should have only one job or responsibility.

# Importance

# Maintainability: Easier to understand and modify.
# Reusability: Components are more focused and can be reused in different contexts.
# Testability: Simplifies writing unit tests as each class has a distinct purpose.

# Violation Example

# Consider a `User` class handling both user data and sending notifications:
# Violates SRP: Handles user data and notifications

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        # Code to save user to the database
        pass
    def send_email(self, message):
        # Code to send email
        pass
    

    
### SRP-Compliant Example
# Separate responsibilities into distinct classes:

# User data management
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        # Code to save user to the database
        pass


# Notification handling
class EmailNotifier:
    def send_email(self, email, message):
        # Code to send email
        pass

# Usage
user = User("Alice", "alice@example.com")
user.save()


notifier = EmailNotifier()
notifier.send_email(user.email, "Welcome!")

# Benefits:
# Modifying email logic won't affect the `User` class.
# EmailNotifier can be reused for other purposes beyond the `User` class.