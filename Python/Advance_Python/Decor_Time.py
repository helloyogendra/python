import time
# from functools import wraps

# def measure_time(func):
#     print("in decorator function name = ", func.__name__)
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
#         return result
#     return wrapper

# # Example usage:
# @measure_time
# def my_function():
#     # Your function code here
#     print("In function - 2")
#     time.sleep(5)

# my_function()

def measure_time1(func):
    print("in decorator function name = ", func.__name__)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


def measure_time2(func):
    print("in decorator function name = ", func.__name__)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


# Example usage:
@measure_time1
def my_function1():
    # Your function code here
    print("In function - 1")
    time.sleep(1)


@measure_time2
def my_function2():
   
    print("In function - 2")

    for _ in range(1_00_000_000):
        pass

    time.sleep(5)



my_function1()

my_function2()


