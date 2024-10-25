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
            print(f"Exception trace : {str(e.__traceback__.tb_lasti)}")
            # You can log the exception here if needed
    return wrapper



@exception_handler
def function_with_exception_handling_1(a, b, c):
    # Your original function code here
    print("Executing function_with_exception_handling_1")
    return a + b + c

@exception_handler
def function_with_exception_handling_2(a, b):
    # Your original function code here
    print("Executing function_with_exception_handling_2")
    return a // b



# Example usage
function_with_exception_handling_1(10, 20, 30)
print("")
function_with_exception_handling_1(10, 20, "30")
print("")

function_with_exception_handling_2(10, 2)
print("")
function_with_exception_handling_2(10, 0)

