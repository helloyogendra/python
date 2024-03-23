import logging

# Decorator for logging
def logger(func1):
    name = func1.__name__
    def wrapper(*args, **kwargs):
        result = func1(*args, **kwargs)
        print(f"Function {name} executed successfully.")
        # You can add more logging details here if needed
        return result
    return wrapper


@logger
def function_with_logging():
    # Your original function code here
    print("Executing function_with_logging")


function_with_logging()
