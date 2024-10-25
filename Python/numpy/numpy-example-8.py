import numpy as np

#Joining the numpy arrays

arr1 = np.array([11, 12, 31, 41])                       #create one 1D array
arr2 = np.array([121, 122, 321, 241])                   #create one 1D array

new_arr = np.concatenate((arr1, arr2))                  # observe (( ))

print(new_arr)


new_arr = np.stack((arr1, arr2), axis=1)
print(new_arr)

new_arr = np.stack((arr1, arr2), axis=0)
print(new_arr)

#Stacking is possible with rows-wise and column-wise

arr1 = np.array([11, 12, 31, 41])                       #create one 1D array
arr2 = np.array([121, 122, 321, 241])                   #create one 1D array

print("-------------------")

new_arr = np.hstack((arr1, arr2))   #rows-wise
print(new_arr)

print("-------------------")

new_arr = np.vstack((arr1, arr2))   #column-wise
print(new_arr)