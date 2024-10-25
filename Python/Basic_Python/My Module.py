#Custom Python Module
#This is a Python module, we will import this module in some other Python Program and we can use these functions
#For a Python Module File, We should use not space in the file name, However it is still possible to use.


def myFunction1(x, y):
    print("myFunction1 called")

    result = x + y
    print(f"sum of {x} and {y} is {result}")


def myFunction2(x):
    print("myFunction2 called")

    result = x * x * x
    return result