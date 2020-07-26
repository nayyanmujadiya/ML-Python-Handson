import numpy as np
import pandas as pd

arr = np.arange(12).reshape((3, 4))

arr

np.concatenate([arr, arr], axis=1)

'''
Suppose we have three Series with no index overlap:
'''

s1 = pd.Series([0, 1], index=['a', 'b'])

s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])

s3 = pd.Series([5, 6], index=['f', 'g'])

'''
Calling concat with these
objects in a list glues together the values and indexes:
'''

pd.concat([s1, s2, s3])

'''
By default concat works along
axis=0 , producing another Series. If
you pass axis=1 , the result will
instead be a DataFrame ( axis=1 is the
columns):
'''
pd.concat([s1, s2, s3], axis=1)


'''
In this case there is no overlap on the other axis, which as you
can see is the sorted union (the 'outer' join) of the indexes. You can instead
intersect them by passing join='inner' :
'''

s4 = pd.concat([s1, s3])

s4

pd.concat([s1, s4], axis=1)

pd.concat([s1, s4], axis=1, join='inner')

'''
In this last example, the 'f' and
'g' labels disappeared because of the
join='inner' option. You can even specify the axes to be used on the other axes with
join_axes :
'''

#pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])

'''
A potential issue is that the concatenated pieces are not
identifiable in the result. Suppose instead you wanted to create a
hierarchical index on the concatenation axis. To do this, use the
keys argument:
'''

result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])

result

result.unstack()

'''
In the case of combining Series along axis=1 , the keys become the DataFrame column headers:
'''

pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three'])


'''
The same logic extends to DataFrame objects:
'''

df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                   columns=['one', 'two'])

df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                   columns=['three', 'four'])
df1

df2

pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])

'''
If you pass a dict of objects instead of a list, the dict’s keys
will be used for the keys option:
'''

pd.concat({'level1': df1, 'level2': df2}, axis=1)

'''
There are additional arguments governing how the hierarchical
index is created. For
example, we can name the created axis levels with the
names argument :
'''

pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
          names=['upper', 'lower'])

'''
A last consideration concerns DataFrames in which the row index
does not contain any relevant data:
'''

df1 = pd.DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])

df2 = pd.DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])

df1

df2

'''
In this case, you can pass ignore_index=True :
'''

pd.concat([df1, df2], ignore_index=True)
