import pandas as pd
import numpy as np

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print(string_data)
print(string_data.isnull())

'''
The built-in Python None value
is also treated as NA in object arrays:
'''

string_data[0] = None
print(string_data.isnull())
