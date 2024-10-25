#List
#Lists are mutable data types - ordered collection/sequence/complex object

list1 = [11, 22, 33, 11, 55, 66, 77]

fruits = ["cherry", "banana", "apple"]

mixed = ["john", 123, 40, "male"]

result = list1[2]
print(result)

list1[2] = 85
print(list1[2])

print(list1)

list1.append(100)   #append a new item at the end of the list
print(list1)

list1.insert(1, 450)   #insert a new item at the given index
print(list1)

myList = [10, 21, 30] + [61, 75]  #concatenate two lists 
print(myList)

for item in myList:
  if item % 2 == 0:
    print(item)

list1 = [11, 22, 33, 11, 55, 66, 77]

print("----slicing---")

result = list1[-4]
print(result)

result = list1[-4:-1]
print(result)

result = list1[1:5]
print(result)

result = list1[:5]
print(result)

result = list1[1:]
print(result)

result = list1[1:7:2]
print(result)

result = list1[::-1]
print(result)
