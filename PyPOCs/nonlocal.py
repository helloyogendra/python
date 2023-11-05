def outer():
    outer_val1 = 1000
    outer_val2 = 200

    def inner (arg):
        nonlocal outer_val1     # nonlocal keyword
        outer_val1 += 100
        arg += 10

        print("inner : outer_val1 = ", outer_val1)
        print("inner : arg = ", arg)
        
    inner(outer_val2)           # calling inner function
    inner(outer_val2)           # calling inner function

    print("outer : outer_val1 = ", outer_val1)
    print("outer : arg = ", outer_val2)
    


# calling outer function
#outer()

# calling outer function
for i in range(3):
    outer()
    

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

    