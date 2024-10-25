import logging

# Decorator for logging
def logger(func1):
    name = func1.__name__

    def wrapper(*args, **kwargs):

        print(f"Function -> {name}, started...")

        result = func1(*args, **kwargs)

        print(f"Function -> {name}, executed successfully...")
        
        # You can add more logging details here if needed
        return result
    return wrapper


@logger
def sample_function_1():
    # Code
    print("Inside sample_function_1")


@logger
def sample_function_2():
    # Code
    print("Inside sample_function_2")


sample_function_1()


sample_function_2()
