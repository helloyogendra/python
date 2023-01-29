# Python day_1
# Data Types - Primitive data type are integer, float, boolean, string
# Variables - are storage/container to store the values
# mutable vs immutable data types

# conditional code execution by using the - if...else, depends upon the outcome of condition(true/false)

a = 10
b = 25
c = 50

isCompleted = False
name = "Alex"

if b > a:
  print("b is bigger")
  print("inside if block")


print("continue with the other code not part of if block")


if name == "John":
  print("found John")
else:
  print("name is different not what we expected")


if name == "John":
  print("found John")
elif name == "Brown":
  print("found Brown")
elif name == "Alex":
  print("found Alex")
else:
  print("name is different not what we expected")


if a <= b: print("a is either less than or it is equal to b")   #shorthand if

# result = condition ? if-true-return-this-value : if-false-return-this-value     #java, c#, c++  #ternary operator

result = "found name"  if name == "John" else "name not found"  
print(result)

name = "John"
result = "found name"  if name == "John" else "name not found"  
print(result)


if c > a and c > b:
  print("c is biggest")
elif b > a and b > c:
  print("b is biggest")
elif a > b and a > c:
  print("a is biggest")
else:
  print("not sure")
  

name = "Alex"

if name == "John" or name == "Brown" or name == "Alex":
  print("found name= ", name)
else:
  print("not found name= ", name)


if name == "John" or name == "Brown" or name == "Bob":
  print("found name= ", name)
else:
  print("not found name= ", name)



#Nested if 

if a < b:
  print("a is less than b")
  if a != c:
    print("a is not equal to c")
    if a == 10:
      print("a is equal to 10")
      print("inner most if block, means all previous are true")

