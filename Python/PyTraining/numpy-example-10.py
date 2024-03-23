#NumPy Search
#We can search an numpy array for a value

import numpy as np

myarr = np.array([11, 23, 56, 67, 34, 89, 56])

result = np.where(myarr == 56)   #it will return the index

print (result)

result = np.where(myarr%2 == 0)   #find the even values and return the index for those values

print (result)


#Search Sorted

list1 = [6, 7, 8, 9]
arr1 = np.array(list1)

result = np.searchsorted(arr1, 7)
print(result)

result = np.searchsorted(arr1, 7, side='right')
print(result)

