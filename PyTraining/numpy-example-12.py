#NumPy Filter

import numpy as np

myarr = np.array([11, 23, 56, 67])  #numpy array object

a = [True, False, False, True]      #list of boolean

result = myarr[a]     #get the values from myarr where a=True for matching index

print(result)


filter = []
myarr1 = np.array([11, 23, 56, 67, 89, 95, 45, 65])  #numpy array object

for items in myarr1:
    if items >= 50:
        filter.append(True)
    else:
        filter.append(False)


result_array = myarr1[filter]
print(result_array)
