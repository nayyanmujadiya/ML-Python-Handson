import numpy as np

F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
# print the first element of F
print(F[0])
# print the last element of F
print(F[-1])

A = np.array([ [3.4, 8.7, 9.9],
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])

print(A[1][0])

tmp = A[1]
print(tmp)
print(tmp[0])

'''
There is another way to access elements of multi-dimensional arrays in Numpy: We use only one pair of square brackets and all the indices are separated by commas:
'''
print(A[1, 0])

'''
The general syntax for a one-dimensional array A looks like this:

A[start:stop:step]
'''

A = np.array([
[11, 12, 13, 14, 15],
[21, 22, 23, 24, 25],
[31, 32, 33, 34, 35],
[41, 42, 43, 44, 45],
[51, 52, 53, 54, 55]])

print(A[:3, 2:])

print(A[3:, :])

print(A[:, 4:])

'''
The following two examples use the third parameter "step".
'''

X = np.arange(28).reshape(4, 7)
print(X)

print(X[::2, ::3])

print(X[::, ::3])

'''
slicings on lists and tuples create new objects, a slicing operation on an array creates a view on the original array.
'''

A = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
S = A[2:6]
S[0] = 22
S[1] = 23
print(A)

'''
Doing the similar thing with lists, we can see that we get a copy:
'''

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = lst[2:6]
lst2[0] = 22
lst2[1] = 23
print(lst)

'''
If you want to check, if two array names share the same memory block, you can use the function np.may_share_memory.
'''

np.may_share_memory(A, S)

A = np.arange(12)
B = A.reshape(3, 4)
A[0] = 42
print(B)

np.may_share_memory(A, B)

'''
The result above is "false positive" example for may_share_memory in the sense that somebody may think that the arrays are the same, which is not the case.
'''
