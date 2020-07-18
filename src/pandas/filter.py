import pandas as pd
from numpy import nan as NA

'''
There are a few ways to filter out missing data. While you always have the option
to do it by hand using pandas.isnull and boolean
indexing, the dropna can be helpful. On a Series, it
returns the Series with only the non-null data and index values:
'''
data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())

#same as
data[data.notnull()]

'''
With DataFrame objects, things are a bit more complex. You may
want to drop rows or columns that are all NA or only those containing
any NAs. dropna by default drops any row containing a missing value:
'''

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],
                     [NA, NA, NA], [NA, 6.5, 3.]])
cleaned = data.dropna()
#print(data)
#print(cleaned)

'''
Passing how='all' will only
drop rows that are all NA:
'''
data.dropna(how='all')

'''
To drop columns in the same way, pass
axis=1 :
'''
data[4] = NA
data
data.dropna(axis=1, how='all')

'''
Suppose you want to keep only rows containing a certain number of observations. You can indicate this with the thresh argument:
'''

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA
df
df.dropna()
df.dropna(thresh=2)
