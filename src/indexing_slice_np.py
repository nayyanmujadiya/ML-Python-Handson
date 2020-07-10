import numpy as np

arr = np.arange(10)
#arr
arr[5]
arr[5:8]
arr[5:8] = 12
#arr
arr_slice = arr[5:8]
arr_slice
arr_slice[1] = 12345
#arr
arr_slice[:] = 64
print(arr)

print(arr[1:6])

#slicing 2d array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2d)

'''
A
slice, therefore, selects a range of elements along an axis. It can be
helpful to read the expression arr2d[:2] as “select
the first two rows of arr2d .”
'''
print(arr2d[:2])
'''
You can pass multiple slices just like you can pass multiple indexes
'''
arr2d[:2, 1:]

'''
When slicing like this, you always obtain array views of the same number of dimensions. By mixing integer indexes and slices, you get lower dimensional slices. For example, I can select the second row but only the first two columns like so:
'''

arr2d[1, :2]

'''
i can select the third column but only first two row.
'''
arr2d[:2, 2]

'''
Note that a colon by itself means to take the entire axis, so you can slice only higher dimensional axes by doing:
'''
arr2d[:, :1]

'''
assigning to a slice expression assigns to the whole selection:
'''
arr2d[:2, 1:] = 0
print(arr2d)
