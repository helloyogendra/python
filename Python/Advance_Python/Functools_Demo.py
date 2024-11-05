import functools as ft


# Reduce
print(ft.reduce(lambda x, y: x + y, [10, 20, 30, 40, 50]))      # 150


# Partial - to simplify function calls when repeatedly need to pass the same argument/s
def multiply(x, y, z):
    return x * y * z


make_it_double = ft.partial(multiply, 2)            # set x = 2 for multiply function

print(make_it_double(4, 5))                            # x=2, y=3, z=4 -> 2 * 3 * 4



# @wraps - helps keep the metadata of the original/decorated function

def my_decorator(f):
    @ft.wraps(f)
    def wrapper(*args, **kwargs):
        print("Before the function call")
        return f(*args, **kwargs)
    return wrapper


@my_decorator
def greet():
    """Prints a greeting."""
    print("Hello!")


print(greet.__name__)  # Output: greet
print(greet.__doc__)   # Output: Prints a greeting.


# lru_cache - to optimize functions that are called frequently with the same arguments, reducing computational overhead by caching results.

@ft.lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Output: 55

print(fibonacci(10))  # Cached result, fast output: 55


# cache - cache() is a decorator that caches the results of function calls. It’s a shorthand for lru_cache(maxsize=None).
# lru_cache vs cache -> when lru_cache reaching the maxsize lru_cache will remove the least-recent-used cache item.

@ft.cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(10))    # no previously cached result, makes 11 recursive calls
print(factorial(5))     # just looks up cached value result, fast output: 120
print(factorial(10))    # makes five new recursive calls, the other 5 are cached


# cached_property() is a decorator for class properties that caches the result of the method, storing it for future access without recomputation.

class Square:
    def __init__(self, side):
        self.side = side

    @ft.cached_property
    def area(self):
        print("Calculating area")
        return self.side ** 2

square = Square(4)
print(square.area)  # Output: Calculating area \n 16
print(square.area)  # Output: 16 (cached result, no recalculation)


# singledispatch() is a decorator that transforms a function into a single-dispatch generic function, 
# allowing different implementations based on the first argument type.

@ft.singledispatch
def process(value):
    print("Default processing")

@process.register(int)
def _(value):
    print("Processing integer:", value)

@process.register(str)
def _(value):
    print("Processing string:", value)


process(10)         # Output: Processing integer: 10
process("hello")    # Output: Processing string: hello


class Single_Dispatch:

    @ft.singledispatchmethod
    def process(self, value):
        print("Single_Dispatch - Default processing ", value)

    @process.register(int)
    def _(self, value):
        print("Single_Dispatch - Processing integer:", value)

    @process.register(str)
    def _(self, value):
        print("Single_Dispatch - Processing string:", value)


object = Single_Dispatch()

object.process([True])  
object.process(10)         # Output: Processing integer: 10
object.process("hello")    # Output: Processing string: hello


# cmp_to_key() converts an old-style comparison function into a key function for use with sorting.


def compare(a, b):
    return (a > b) - (a < b)
sorted_list = sorted([33, 22, 44, 11], key=ft.cmp_to_key(compare))

print(sorted_list)  