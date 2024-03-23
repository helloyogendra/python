#List

name = "John"
age = 32

list1 = [10, 20, 30, 40, 55, 66, 88]

#Removing list items::

list1.remove(40)  #remove this value
print(list1)

list1.pop(2)  #remove value at this index
print(list1)

list1.pop()    #remove the last value from list
print(list1)

del list1[0]   #delete the list item at index=0
print(list1)

result = list1.clear()   #it is not returning anything, it is in place modification
print(result)            #
print(type(result))

print(type(list1))       #type of list1 is still list-type
print(list1)              #empty list

del list1
del name
del age

#print(list1)  #list1 is deleted, we can not access it now
#print(name)    #name is deleted, we can not access it now
#print(age)     #age is deleted, we can not access it now

print("---list sorting examples--------------")

#Sorting list
list1 = [10, 25, 80, 90, 15, 36, 88]
result = sorted(list1)  # not the in-place sorting, means returns a new sorted object

print(list1) 
print(result) 

list1.sort()   # in-place sorting, means sort the original object
print(list1) 

list1.sort(reverse= True)   # in-place sorting, means sort the original object
print(list1) 


#Copying lists

list1 = [10, 25, 80, 90, 15, 36, 88]

print(list1)

print("---list copy examples--------------")

#both lists are referenced to the same location, 
#if we modify any of the list, changes will automatically reflect to the other list
#below is not an actual copy
list2 = list1  

list2[0] = 100

print(list1)
print(list2)

#make a copy by using the list.copy() method
list3 = list1.copy()

list3[0] = 99

print(list1)
print(list2)

print(list3)


#make a copy by using the in-built method = list()
list4 = list(list3)

list4[0] = 299

print(list3)
print(list4)

