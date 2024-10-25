# Functions as Objects
#
# Closures
# In a nested function construct, 
# an inner function can remember the state of variables from surrounding scope even after outer function execution is completed


# Nested function

def outer(txt):

    def inner():
        print(txt)
    return inner


store_inner = outer('Hello')   # executing outer

store_inner()                  # store_inner is storing the function 'inner', 'outer' function execution is completed but inner can still access 'txt'



# Anothe example:

def outer_func(n):

    def inner_func(x):
        return x * n
    
    return inner_func


func_one = outer_func(3)
func_two = outer_func(7)

print(func_one(3))
print(func_two(5))


#Closure example::
def closure():
    outer_val1 = 1000

    def inner ():
        nonlocal outer_val1     # nonlocal keyword
        outer_val1 += 100
        print("inner : outer_val1 = ", outer_val1)
        
    return inner



# calling closure function
print("testing closure function")

func = closure()
del closure

func()  #1100
func()  #1200
func()  #1300

