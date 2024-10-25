#Custom Python Module
#This is a Python module, we will import this module in some other Python Program and we can use these functions


def myFunction1(x, y):
    print("myFunction1 called")

    result = x + y
    print(f"sum of {x} and {y} is {result}")


def myFunction2(x):
    print("myFunction2 called")

    result = x * x * x
    return result