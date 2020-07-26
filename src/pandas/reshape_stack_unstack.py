import pandas as pd
import numpy as np
'''
Consider a small DataFrame with string arrays as row and column
indexes:
'''

data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'],
                    name='number'))

data

'''
Using the stack method
on this data pivots the columns into the rows, producing a
Series:
'''
result = data.stack()

result

'''
From a hierarchically indexed Series, you can rearrange the data
back into a DataFrame
with unstack :
'''

result.unstack()

'''
By default the innermost level is unstacked (same with stack ). You can unstack a different level by
passing a level number or name:
'''

result.unstack(0)

result.unstack('state')

'''
Unstacking might introduce missing data if all of the values in
the level aren’t found in each of the subgroups:
'''

s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])

data2 = pd.concat([s1, s2], keys=['one', 'two'])

data2

data2.unstack()

'''
Stacking filters out missing data by default, so the operation is
more easily invertible:
'''

data2.unstack()

data2.unstack().stack()

data2.unstack().stack(dropna=False)

'''
When you unstack in a DataFrame, the level unstacked becomes the
lowest level in the result:
'''

df = pd.DataFrame({'left': result, 'right': result + 5},
                  columns=pd.Index(['left', 'right'], name='side'))
df
df.unstack('state')

'''
When calling stack , we can indicate the name of
the axis to stack:
'''

df.unstack('state').stack('side')
