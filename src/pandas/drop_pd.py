import pandas as pd
import numpy as np

obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
print(obj)
new_obj = obj.drop('c')
print(new_obj)
obj.drop(['d', 'c'])
print(obj)

'''
With DataFrame, index values can be deleted from either axis. To
illustrate this, we first create an example DataFrame:
'''

data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)

data.drop(['Colorado', 'Ohio'])
print(data)

'''
You can drop values from the columns by passing
axis=1 or axis='columns' :
'''
data.drop('two', axis=1)
data.drop(['two', 'four'], axis='columns')
print(data)

'''
Many functions, like drop , which modify the
size or shape of a Series or DataFrame, can manipulate an object
in-place without returning a new object:
'''
obj.drop('c', inplace=True)
print(obj)
