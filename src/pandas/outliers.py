import pandas as pd

'''
Consider a DataFrame with some normally distributed data:
'''

data = pd.DataFrame(np.random.randn(1000, 4))
data.describe()

'''
Suppose you wanted to find values in one of the columns exceeding
3 in absolute value:
'''

col = data[2]
col[np.abs(col) > 3]

'''
To select all rows having a value exceeding 3 or –3, you can use
the any method on a
boolean DataFrame:
'''

data[(np.abs(data) > 3).any(1)]

'''
Values can be set based on these criteria. Here is code to cap
values outside the interval –3 to 3:
'''

data[np.abs(data) > 3] = np.sign(data) * 3
data.describe()

'''
The statement np.sign(data) produces 1 and –1 values based on whether the values in
data are
positive or negative:
'''

np.sign(data).head()
