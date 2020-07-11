import pandas as pd
import numpy as np

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)

print(obj2['a'])
obj2['d'] = 6
print(obj2[['c', 'a', 'd']])

print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))
'''
Another way to think about a Series is as a fixed-length, ordered dict, as it is a mapping of index values to data values. It can be used in many contexts where you might use a dict:
'''
print('b' in obj2)
print('e' in obj2)
