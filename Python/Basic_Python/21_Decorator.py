# Function Decorator
# By using this feature we can modify the the behaviour/functionality of an existing function.
# We will not modify the code of our exisitng/old function.
# We will introduce a new function (wrapper function/decorator), this new wrapper function will wrap the old function

# In Python we can define nested function (function inside function)
# Like input arguments (function parameters), we can pass functiona name as a parameter in python
# We can return a value from a function, we can also return a function from a function

#this is a standard function, expecting a single parameter/argument and returning a value
def stdFunction(x):
  result = x*x*x
  return result

res = stdFunction(10)   #calling our standard function, res will hold the returned value, here that is 1000


#Nested Function
def outerFunction(num):
  def innerFunction(count):
    result = num * count
    return result
  return innerFunction            #here we are returning a function and not a value



store_inner_function = outerFunction(10)   # here 'outerFunction' is returning a function and not a value, so 'store_inner_function' will become a function

final_result = store_inner_function(5)    # here in this line we are calling the - 'innerFunction'

print(final_result)

# innerFunction(5)        # error here, innerFunction is not available for outside, it is local inside outerFunction


#Passing Function as an argument
#We can pass a function as an argument to another function in Python

#define a standard function
def sum(a, b):
  return a + b

rs = sum(10, 20)  #calling the sum function, rs is 30 here

print(f"calling the sum function directly, result is= {rs}")

#this function is accepting a function name as first parameter
def calculation(func, x, y):
  result = func(x, y)
  return result * result


#calling the calculation function now, here first parameter is name of an existing function, that is 'sum' function
result = calculation(sum, 10, 20)
print(result)

print("---------Decorator-Example--1----------------")

#Decorator-Example-1
# A decorator will accept a function as a parameter and it can produce a new function by adding some new functionalities

#define a decorator function
def myDecorator(func):
  def inner():
    print("inside decorator...")
    func()
    print("func called inside decorator...")

  return inner


#define a standard/normal/ordinary function
def myfunc():
  print("I am a standard function")


myfunc()             #calling the standard function directly without decorator

new_function = myDecorator(myfunc)  #applying the decorator

new_function()              #calling the modified function

print("---------Decorator-Example--2----------------")

#Decorator-Example-2

def decoratorFunc(function):
  def nestedFunction(x):
    print("decorator, here x is, ", x)
    rs = function(x * 2)
    return rs
  return nestedFunction

@decoratorFunc      #applying the decorator function=decoratorFunc on top of standard function=stdFunc
def stdFunc(x):
  print("standard, here x is=", x)
  return x*x


result = stdFunc(2)
print(result)

