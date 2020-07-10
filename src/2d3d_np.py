import numpy as np

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(arr2d[2])

print(arr2d[0][2])
print(arr2d[0, 2])

# 2 x 2 x 3
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)

# 2 x 3
print(arr3d[0])

# make a copy
old_values = arr3d[0].copy()
arr3d[0] = 42
print(arr3d)
arr3d[0] = old_values
print(arr3d)

# one step
print(arr3d[1, 0])

# same in two step
x = arr3d[1]
print(x)
print(x[0])

'''
Note that in all of these cases where subsections of the array have been selected, the returned arrays are views.
'''


