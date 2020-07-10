import numpy as np
from sys import getsizeof as size
#with element
a = np.array([24, 12, 57])
print(size(a))

#empty
e = np.array([])
print(size(e))

'''
We can see that the difference between the empty array "e" and the array "a" with three integers consists in 24 Bytes. This means that an arbitrary integer array of length "n" in numpy needs

96 + n * 8 Bytes

whereas a list of integers needs, as we have seen before

64 + 8 len(lst) + len(lst) 28

This is a minimum estimation, as Python integers can use more than 28 bytes.
'''

'''
When we define a Numpy array, numpy automatically chooses a fixed integer size. In our example "int64".
'''

a = np.array([24, 12, 57], np.int8)
print(size(a) - 96)

a = np.array([24, 12, 57], np.int16)
print(size(a) - 96)

a = np.array([24, 12, 57], np.int32)
print(size(a) - 96)

a = np.array([24, 12, 57], np.int64)
print(size(a) - 96)
