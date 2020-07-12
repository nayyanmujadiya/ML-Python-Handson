import pandas as pd

'''
If the nested dict is passed to the DataFrame, pandas will interpret the outer dict keys as the columns and the inner keys as the row indices:
'''
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = pd.DataFrame(pop)
frame3

'''
You can transpose the DataFrame (swap rows and columns) with
similar syntax to a NumPy array:
'''
frame3.T
