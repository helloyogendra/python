# Python Closures
# Closures are function objects that remembers values in the enclosing scope

def outerFunction(param):

    def innerFunction():
        print(param)
    
    innerFunction()


outerFunction("Good Day")   #inside outer function definition we have defined the inner function and calling the inner function


def outerFunction2(param):

    def innerFunction():
        print(param)
    
    return innerFunction      #we are returning the inner function


func = outerFunction2("Hello")   #we are storing the inner function in func

func()


#nonlocal example

def outerFunction3():
    val = "Monday"

    def innerFunction():
        val = "Tuesday"
        print(val)
    
    innerFunction()
    return val;


result = outerFunction3()
print(result)


def outerFunction4():
    val = "Monday"

    def innerFunction():
        nonlocal val
        val = "Tuesday"
        print(val)
    
    innerFunction()
    return val;


result = outerFunction4()
print(result)



def outerFunction5():
    val = "Saturday"

    def innerFunction():
        nonlocal val
        val = "Sunday"
        print(val)
    
    return innerFunction;


func1 = outerFunction5()

del outerFunction5

func1()


# non local is useful for nested function
# global is useful when we are interested in a global variable to use inside a function