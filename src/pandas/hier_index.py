import pandas as pd
import numpy as np

'''
Let’s start with a simple
example; create a Series with a list of lists (or arrays) as the
index:
'''
data = pd.Series(np.random.randn(9),
                 index=[['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'd'],
                        [1, 2, 3, 1, 3, 1, 2, 2, 3]])
#print(data)

#print(data.index)

'''
With a hierarchically indexed object, so-called
partial indexing is possible, enabling you to
concisely select subsets of the data:
'''

#print(data['b'])
#print(data['b':'c'])
#print(data.loc[['b', 'd']])

'''
Selection is even possible from an “inner” level:
'''

#print(data.loc[:, 2])


'''
Hierarchical indexing plays an important role in reshaping data and
group-based operations like forming a pivot table. For example, you could rearrange the data
into a DataFrame using its unstack method:
'''

#print(data.unstack())

'''
The inverse operation of unstack is stack:
'''

#print(data.unstack().stack())

'''
With a DataFrame, either axis can have a hierarchical index:
'''

frame = pd.DataFrame(np.arange(12).reshape((4, 3)),
                     index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                     columns=[['Ohio', 'Ohio', 'Colorado'],
                              ['Green', 'Red', 'Green']])
#print(frame)


'''
The hierarchical levels can have names (as strings or any Python
objects).
'''

frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']
#print(frame)

'''
With partial column indexing you can similarly select groups of
columns:
'''
#print(frame['Ohio'])

'''
A MultiIndex can be created by
itself and then reused; the columns in the preceding DataFrame with level
names could be created like this:
'''

#pd.MultiIndex.from_arrays([['Ohio', 'Ohio', 'Colorado'], ['Green', 'Red', 'Green']], names=['state', 'color'])

