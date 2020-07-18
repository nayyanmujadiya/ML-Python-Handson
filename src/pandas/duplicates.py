import pandas as pd

'''
duplicate rows may be found in a DataFrame for any
number of reason.
'''

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],
                     'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)

'''
The DataFrame method duplicated returns a boolean Series indicating whether each row is a
duplicate (has been observed in a previous row) or not:
'''
data.duplicated()

'''
Relatedly, drop_duplicates returns a DataFrame where the duplicated array is False :
'''
data.drop_duplicates()

'''
Both of these methods by default consider all of the columns;
alternatively, you can specify any subset of them to detect duplicates.
Suppose we had an additional column of values and wanted to filter
duplicates only based on the 'k1' column:
'''

data['v1'] = range(7)
data.drop_duplicates(['k1'])

'''
duplicated and drop_duplicates by default keep the first
observed value combination. Passing keep='last' will return the last one:
'''

data.drop_duplicates(['k1', 'k2'], keep='last')
