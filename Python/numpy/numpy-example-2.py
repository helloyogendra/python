import numpy as np

tpl1 = (100, 150, 350, 333, 444, 25, 75)    #tuple object

arr2 = np.array(tpl1)       #creating a new numpy array object 

#Slicing  - array[start:end]   or  array[start:end:step]

result = arr2[1:4]     #get values from index=1 till index=4-1
print(result)

result = arr2[:4]     #get values from index=0 till index=4-1
print(result)

result = arr2[1:]     #get values from index=1 till last index
print(result)

result = arr2[1:6:2]  #get values from index=1 till last index=6-1, step/skips=2
print(result)


result = arr2[-5:-1]     #negative slicing
print(result)


#Slicing two-D arrays

numpyArray = np.array([ [10, 20, 30, 40, 50] , [11, 22, 33, 44, 55], [15, 25, 67, 89, 98] ])

result = numpyArray[0, 1:4]    # from first list slice for 1:4 (get values from index=1 till index=4-1)

print("result from 2D slice=  ", result)


result = numpyArray[0:2, 1:4]    # numpyArray[0:2 means range of lists, 1:4 means range of values in a list] 
print("2D slice=  ", result)