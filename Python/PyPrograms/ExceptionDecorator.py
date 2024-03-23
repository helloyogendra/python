import logging

# Decorator for exception handling
def exception_handler(func):
    name = func.__name__
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Exception in line {str(e.__traceback__.tb_lineno)}")
            print(f"Exception in function {name}: {str(e)}")
            # You can log the exception here if needed
    return wrapper



@exception_handler
def function_with_exception_handling(a, b, c):
    # Your original function code here
    print("Executing function_with_exception_handling")
    return a + b + c



# Example usage
function_with_exception_handling(10, 20, 30)
function_with_exception_handling(10, 20, "30")

