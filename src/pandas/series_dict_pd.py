import pandas as pd

d = {'one': pd.Series([1,2,3], index=['a','b','c']),
     'tow': pd.Series([1,2,3,4], index=['a','b','c','d'])}

df = pd.DataFrame(d)
print(df)
