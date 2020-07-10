import numpy as np

arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])
# assign scalar to slice
arr[5:8] = 12
print(arr)

'''
An important first distinction from Python’s built-in lists is that array slices are views on the original array. This means that the data is not copied, and any modifications to the view will be reflected in the source array.
'''

arr_slice = arr[5:8]
print(arr_slice)

arr_slice[1] = 12345
print(arr)

'''
The “bare” slice [:] will assign to all values in an array:
'''
arr_slice[:] = 64
print(arr)

'''
If you want a copy of a slice of an ndarray instead of a view, you will need to explicitly copy the array for example, arr[5:8].copy().
'''
