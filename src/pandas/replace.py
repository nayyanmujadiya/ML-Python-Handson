import pandas as pd

data = pd.Series([1., -999., 2., -999., -1000., 3.])
data

'''
The -999 values might be
sentinel values for missing data. To replace these with NA values that
pandas understands, we can use replace , producing a new Series (unless you
pass inplace=True ):
'''
data.replace(-999, np.nan)

'''
If you want to replace multiple values at once, you instead pass a
list and then the substitute value:
'''

data.replace([-999, -1000], np.nan)

'''
To use a different replacement for each value, pass a list of
substitutes:
'''

data.replace([-999, -1000], [np.nan, 0])

'''
The argument passed can also be a dict:
'''

data.replace({-999: np.nan, -1000: 0})
