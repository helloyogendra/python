# Python day_1
# Data Types - Primitive data type are integer, float, boolean, string
# Variables - are storage/container to store the values
# mutable vs immutable data types

firstName = "John"    #declared a variable where name of that variable is 'firstName' and data-type of that variable is string and stored value is 'John'
grade = 'A'           #declared a variable where name of that variable is 'grade' and data-type of that variable is string and stored value is 'A'

count = 10
price = 55.55

# print(count + grade)   #error here why? two different types

print(str(count) + grade)   #now no error

print(type(count))    #get the type of a variable by using the type() function

count = "ten"
print(type(count))

isCompleted = True    #bool variable example

print(type(grade))

a = 1
b = 1
c = 1

print(a)
print(a + b + c)

print(id(a))      #get the memory address of a variable by using the id() function
print(id(b))
print(id(c))

a = 12

print(id(a))
print(id(b))
print(id(c))

