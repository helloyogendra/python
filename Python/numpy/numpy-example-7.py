import numpy as np

#Iterating/Loop

arr1 = np.array([11, 12, 31, 41])                   #create one 1D array

for items in arr1:
    print(items)


arr2 = np.array([ [15, 12, 31, 41], [11, 12, 31, 45] ])                   #create one 2D array

for items in arr2:
    print(items)

print("-------------------")
#loop through a 2d array to get all values
for items in arr2:
    for i in items:
        print(i)


#with each new domension of array, we need one more for-loop, that is not a good idea

print("-------------------")

#using the nditer() method from numpy to loop through

arr2 = np.array([ [15, 12, 31, 41], [11, 12, 31, 45] ])                   #create one 2D array


#it will work with n-dimensions, nested for-loops are not required
for x in np.nditer(arr2):
    print(x)


print("---ndenumerate will give index and associated values----------------")


for i, val in np.ndenumerate(arr2):
    print(f" at index={i} the value is {val}")

