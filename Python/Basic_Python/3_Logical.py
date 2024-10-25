# Python day_1
# Data Types - Primitive data type are integer, float, boolean, string
# Variables - are storage/container to store the values
# mutable vs immutable data types

# Operators
# Logical and comparison operators


x = 5
y = 7

print(x == y)         #checks if values of x and y are equal
print(11 == 11)       #checks if these two values are equal
print(11 == (5+4+2))  #checks if value from left hand side is equal to the result of expression from right hand side

result = 11 == (x + 4 + 2)

print("value of result variable is= ", result)
print("data type of result variable is= ", type(result))

print(x != y)         #checks if values of x and y are not equal
print(11 != 11) 

print(x > y)           #checks if values of x is greater than the value of y  
print(x < y)           #checks if values of x is less than the value of y   

print(x >= y)         #checks if values of x is greater than or equal to the value of y   
print(x <= y)         #checks if values of x is greater than or equal to the value of y    

print("Logical and operator")

print(x > 3 and x > 2)                          #True only if both conditions are true
print(x > 3 and x > 5)

print(x > 3 and x > 2 and x < 10 and x == 5)   #True only if all conditions with 'and' are true

print("Logical or operator")

print(x > 3 or x > 2)                          #True even if a single condition is true
print(x < 3 or x < 5)                          #False when all conditions are false 

print(x < 3 or x < 2 or x == 10 or x == 5)     #True even if a single condition is true

print("Logical not operator")

print(x > 3 and x < 10)          #observe behaviour/output without 'not' operator
print( not (x > 3 and x < 10))   #observe behaviour/output with 'not' operator