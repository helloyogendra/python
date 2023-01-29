#Functions
#Wrting our custom functions

#define a function, name of this function is = functionName
def functionName():
  print("inside function")
  print("function is called")
  print("just a simple example")

#calling/executing our function 3 times, uncomment below 2 lines
#functionName()
#functionName()
functionName()

#in the below loop, it will execute the function for each cycle for this loop
for i in range(5):
  #functionName()
  pass

#define a function where name is 'calc' and this function is accepting 3 arguments/parameters
def calc(check, b, c):
  if check == True:
    return b + c
  else:
    return b - c

#call the 'calc' function
result = calc(True, 10, 25)
print(result)

x = 85
y = 55

result = calc(x > y, x, y)   #first parameter is condition which will produce True or False
print(result)

result = calc(x < y, x, y)   #first parameter is condition which will produce True or False
print(result)


#Define a Function with a default parameter, default parameter will come at last [extreme right side], here y is a default parameter
def getPower(x, y=2):
  result = x ** y
  return result


print( getPower(3, 3) )  #this function is expecting two parameters, here x=3 and y=3

print( getPower(4) )     #this function is expecting two parameters, here x=4 and y=2, y=2 it will take from default parameter


#Assignment: define a function with 3 parameters, two paremeters should be default parameter

#example - returning multiple values from a function
def getCalculatedValues(val1, val2):
  a = val1 + val2
  b = val1 - val2
  c = val1 * val2
  d = val1 // val2
  return(a, b, c, d)


a1, a2, a3, a4 = getCalculatedValues(20, 2)   #capturing the multiple returned values

print(f"sum is {a1} product is {a3}")

#Assignment: 
#change the above function to return more or less values
#for the above function capture the result in a single variable and check type of that variable using type function
