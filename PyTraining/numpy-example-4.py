import numpy as np

#NumPy has some additional data types

arr1 = np.array([1, 2, 3, 4])

print(arr1.dtype)

arr2 = np.array(['Apple', 'Cherry', 'banana'])

print(arr2.dtype)


list1 = [1, 2, 3, 4, 5]

arr3 = np.array(list1, dtype='U6')   #unicode string
print(arr3)
print(arr3[1])

list2 = ['12', '25', '23']

arr4 = np.array(list2, dtype='i')   # i means integer data type
print(arr4)
print(arr4[1])

#list2 = ['12', '25', 'dd']             # i means integer data type, error here, list2 is having a non-number item
#arr4 = np.array(list2, dtype='i')


#changing the data type of already exisitng numpy arrays

arr5 = np.array([10, 20, 30, 40])

new_array = arr5.astype('f')  #convert the type of numpy array from int to float

print(new_array)
print(new_array.dtype)


arr5 = np.array([10.1, 20.25, 30.0, 40.88])

new_array = arr5.astype('i')  #convert the type of numpy array from float to int

print(new_array)
print(new_array.dtype)


arr5 = np.array([10, 0, 9, 2, 0, 11])

new_array = arr5.astype(bool)  #convert the type of numpy array from int to bool

print(new_array)
print(new_array.dtype)