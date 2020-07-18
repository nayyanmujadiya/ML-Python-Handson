import pandas as pd

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
df

df.fillna(0)

'''
Calling fillna with a dict, you
can use a different fill value for each column:
'''
df.fillna({1: 0.5, 2: 0})

'''
fillna returns a new object, but you can modify
the existing object in-place:
'''


_ = df.fillna(0, inplace=True)
df

'''
The same interpolation methods available for reindexing can be
used with fillna :
'''

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA
df
df.fillna(method='ffill')
df.fillna(method='ffill', limit=2)

'''
With fillna you can do lots of
other things with a little creativity. For example, you might pass the
mean or median value of a Series:
'''

data = pd.Series([1., NA, 3.5, NA, 7])
data.fillna(data.mean())
