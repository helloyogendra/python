import numpy as np

#Slicing two-D arrays

numpyArray = np.array([ [10, 20, 30, 40, 50] , [11, 22, 33, 44, 55], [15, 25, 67, 89, 98] ])

result = numpyArray[0, 1:4]    # from first list slice for 1:4 (get values from index=1 till index=4-1)

print("result from 2D slice=  ", result)


result = numpyArray[0:2, 0:4]    # numpyArray[0:3 means range of lists, 0:4 means range of values in a list] 
print("2D slice=  ", result)


result = numpyArray[0:3, 1]    # numpyArray[0:3 means range of lists, 1 means, get value at index=1 from the range of that list] 
print("get items from two lists, for same index=  ", result)

#get just one item
result = numpyArray[1, 1]     
print("get one item from 2d array=  ", result)

