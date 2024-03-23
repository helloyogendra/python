import numpy as np

# Numpy - Array Copy vs View
# Copy will produce a new array, modifying the new array will not impact the original array
# View - view is like an alias for the original array, modifying the original array will impact the view

arr1 = np.array([11, 12, 31, 41])   #create an array

new_arr = arr1.copy()               #make a copy of the above array object
arr1[1] = 27                        #modify the original array object

print(arr1)
print(new_arr)
print("for copy =new_arr the base is this-> ", new_arr.base)



arr2 = np.array([111, 112, 131, 141])   #create an array

new_arr1 = arr2.view()               #make a view of the above array object
arr2[1] = 27                         #modify the original array object

print(arr2)
print(new_arr1)
print("for view=new_arr1 the base is this-> ", new_arr1.base)

new_arr1[0] = 127 
print(arr2)
print(new_arr1)

