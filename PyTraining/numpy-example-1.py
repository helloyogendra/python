import numpy as np

# print(numpy)
# conda create --name myenv python=3.9
# conda activate myenv
# pip install numpy
# Visula Studio Code - Press Ctrl + Shift + P and "Select Interpretor"


list1 = [10, 20, 30, 45, 75]        #python list object
tpl1 = (100, 150, 350, 333, 444)    #tuple object

arr1 = np.array(list1)       #creating a new numpy array object 
arr2 = np.array(tpl1)       #creating a new numpy array object 

print(type(arr1))
print(np.__version__)

print(arr1)
print(arr2)

item = arr1[3]       #get value from 3rd index of numpy array object

print(arr1[0] + arr1[-1])


# using numpy library we can create array with dimensions:

arr3 = np.array(55)   # 0-D array - single value / scalar

# arr1 and arr2 variables/objects are 1-D arrays

list2 = [[11, 22, 33, 44, 55], [10, 20, 30, 40, 50]]

two_D_arr = np.array(list2)

print(two_D_arr.ndim)

print(two_D_arr[0, 0])  #first index is the index of whole list (first list), second index is pointing to the values/items from that list

print(two_D_arr[1, 1])  #first index is the index of whole list (second list), second index is pointing to the values/items from that list

print(two_D_arr[-1, -1])  #from last list, get the last item

#Slicing  - array[start:end]   or  array[start:end:step]



