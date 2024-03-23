import numpy as np

# Numpy - Shape = shape of an array is the number of elements in each dimension


arr1 = np.array([11, 12, 31, 41])                   #create one 1D array

print(arr1.shape)

arr1 = np.array([ [11, 12, 31, 41], [11, 12, 31, 41] ])   #create a 2D array

print(arr1.shape)


arr2 = np.array([11, 12, 31, 41], ndmin=2)   
print(arr2)


#Reshaping the numpy arrays

list1 = [17, 22, 33, 44, 55, 66, 77, 88, 99, 12, 19, 20]

new_arr = np.array(list1)

result = new_arr.reshape(4,3)  #create 4 lists each list having 3 items
print(result)


