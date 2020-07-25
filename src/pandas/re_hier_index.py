import pandas as pd
import numpy as np

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
#print(frame)

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

print(frame)

'''
The swaplevel takes two level numbers or names and
returns a new object with the levels interchanged (but the data is
otherwise unaltered ):
'''

print(frame.swaplevel('key1', 'key2'))

'''
sort_index , on the other hand,
sorts the data using only the values in a single level. When swapping
levels, it’s not uncommon to also use sort_index so that the result is
lexicographically sorted by the indicated level:
'''

print(frame.sort_index(level=1))

print(frame.swaplevel(0, 1).sort_index(level=0))

'''
Summary Statistics by Level
Under the hood, this utilizes pandas’s
groupby machinery,
'''

print(frame.sum(level='key2'))
print(frame.sum(level='color', axis=1))


