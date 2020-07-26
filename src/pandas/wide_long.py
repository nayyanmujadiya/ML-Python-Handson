import pandas as pd
#import numpy as np

df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})

df


'''
The key column may be a group indicator, and the other columns are data values. when usiing pandas.melt, we must indicate which columns if any are group indicators. Let's use key as the only group indicator here:
'''

melted = pd.melt(df, ['key'])

melted

'''
Using pivot , we can reshape back to the
original layout:
'''

reshaped = melted.pivot('key', 'variable', 'value')

reshaped

'''
Since the result of pivot creates an index from
the column used as the row labels, we may want to use
reset_index to move the data back into a column:
'''

reshaped.reset_index()

'''
You can also specify a subset of columns to use as value
columns:
'''

pd.melt(df, id_vars=['key'], value_vars=['A', 'B'])

'''
pandas.melt can be used without any group
identifiers, too:
'''

pd.melt(df, value_vars=['A', 'B', 'C'])

pd.melt(df, value_vars=['key', 'A', 'B'])
