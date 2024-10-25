import numpy as np

#Splitting the numpy arrays

arr1 = np.array([11, 12, 31, 41, 56, 78])                       #create one 1D array

newarr = np.array_split(arr1, 2)
print(newarr)

newarr = np.array_split(arr1, 4)    #if 4 equal array can not be created it will adjust from th end
print(newarr)

print(newarr[0])


arr2 = np.array([[11, 12, 31, 41, 56, 78], [10, 12, 31, 41, 56, 80]])      #2D array

newarr1 = np.array_split(arr2, 3)    
print(newarr1)

