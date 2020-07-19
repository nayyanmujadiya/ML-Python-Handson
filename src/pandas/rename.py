import pandas as pd

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])

'''
Like a Series, the axis indexes have a map method:
'''
transform = lambda x: x[:4].upper()
data.index.map(transform)

'''
You can assign to index ,
modifying the DataFrame in-place:
'''

data.index = data.index.map(transform)
data

'''
If you want to create a transformed version of a dataset without modifying the
original, a useful method is rename :
'''

data.rename(index=str.title, columns=str.upper)

'''
Notably, rename can be used in
conjunction with a dict-like object providing new values for a subset of
the axis labels:
'''

data.rename(index={'OHIO': 'INDIANA'},
            columns={'three': 'peekaboo'})

'''
rename saves you from the chore
of copying the DataFrame manually and assigning to its index and columns attributes. Should you wish to modify
a dataset in-place, pass inplace=True :
'''

data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
data
