import numpy as np

a = np.array([[1,2],[3,4],[5,6]])

'''
find the elements of A that are bigger then 2
this returns a numpy array of boolean ot the same shape as a
where each slot of bool_indx tells whether that element of a is > 2.
'''
bool_idx = (a>2)

print(bool_idx)

print(a[bool_idx])

print(a[a>2])
