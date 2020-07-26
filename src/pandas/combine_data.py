import numpy as np
import pandas as pd
'''
You may have two datasets whose
indexes overlap in full or part. As a motivating example, consider
NumPy’s where function,
which performs the array-oriented equivalent of an if-else
expression:
'''

a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])

b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])

b[-1] = np.nan

a

b

np.where(pd.isnull(a), b, a)

'''
Series has a combine_first method, which performs the equivalent of this operation along with
pandas’s usual data alignment logic:
'''

b[:-2].combine_first(a[2:])

#b.combine_first(a)

'''
With DataFrames, combine_first does the same thing column by column, so you can think of it as
“patching” missing data in the calling object with data from the object
you pass:
'''

df1 = pd.DataFrame({'a': [1., np.nan, 5., np.nan],
                    'b': [np.nan, 2., np.nan, 6.],
                    'c': range(2, 18, 4)})

df2 = pd.DataFrame({'a': [5., 4., np.nan, 3., 7.],
                    'b': [np.nan, 3., 4., 6., 8.]})
df1

df2

df1.combine_first(df2)
