import pandas as pd
import numpy as np
'''
There are many ways to create dataframe. most common is from a dict of
equal-length list or NumPy arrays
'''

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
# sorted order
print(frame)
print(frame.head(2))
'''
If you specify a sequence of columns, the DataFrame’s columns will be arranged in that order:
'''
f = pd.DataFrame(data, columns=['year', 'state', 'pop'])
print(f)

'''
If you pass a column that isn’t contained in the dict, it will appear with missing values in the result:
'''

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four',
                             'five', 'six'])
print(frame2)
print(frame2.columns)

'''
A column in a DataFrame can be retrieved as a Series either by dict-like notation or by attribute:
'''
print(frame2['state'])
print(frame2.year)

'''
Rows can also be retrieved by position or name with the special loc attribute
'''
frame2.loc['three']

'''
Columns can be modified by assignment. For example, the empty 'debt' column could be assigned a scalar value or an array of values:
'''

frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(6.)
print(frame2)

'''
When you are assigning lists or arrays to a column, the value’s length
must match the length of the DataFrame. If you assign a Series, its
labels will be realigned exactly to the DataFrame’s index, inserting
missing values in any holes:
'''

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

'''
boolean values where the state column equals
'Ohio' :
'''

frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

#now, to remove this column
del frame2['eastern']
print(frame2.columns)
