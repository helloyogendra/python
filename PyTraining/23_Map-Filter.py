# Map, Filter & Reduce Function:

#Map - function, we can apply on top of a collection and we can transform it.

#Map-example2-with standard Function

list1 = [15, 10, 5, 11, 7, 5, 4]

def func(a):
  rs = a*a*a
  return rs

# myfunc = lambda x,y,z: x+y+z   # a lambda function with 3 parameters/arguments

result = map(func, list1)   #returns a map object

print(result)    
print(list(result))

#Map-example2-with Lambda Function
#in below example we are using a lambda function or we can also say anonymous function
result = map(lambda x: x*x, list1)

new_list = list(result)
print(new_list)

print(list(map(lambda x: x*x*x, list1)))  #example-3-all in one line


#Reduce Function
#Operates on top of a collection object and returns a single value

from functools import reduce

list2 = [15, 10, 5, 11]

result = reduce(lambda a, b: a + b, list2)

print("Reduced value is= ", result)



#Filter Function
#By using the filter function we can filter the items of a collection like list

list3 = [15, 10, 5, 11, 12]

result = filter(lambda x: True if x % 2==0 else False, list3)

print(list(result))

#Assignment:
#write a standard function which accepts a single parameter
#inside this function check if that parameter is a odd number or even number
#return if it is an odd number
#pass that function to your filter function





