#NumPy Sort

import numpy as np

myarr = np.array([11, 23, 56, 67, 34, 89, 56])

print(np.sort(myarr))   #sort and return a new array object

print(myarr)


myarr = np.array(["Car", "Truck", "SUV", "Bus"])

result = np.sort(myarr)   #sort and return a new array object

print(result)
print(myarr)


#Sorting the 2D array

myarr = np.array([[11, 83, 56], [67, 34, 89]])

print(np.sort(myarr))   #both dimensions should have the same length

print(myarr)