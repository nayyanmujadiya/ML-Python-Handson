import pandas as pd

d = {'one': pd.Series([1,2,3], index=['a','b','c']),
     'tow': pd.Series([1,2,3,4], index=['a','b','c','d'])}

df = pd.DataFrame(d)

# select one row
print(df.loc['b'])

# select multiple row
print(df[2:4])

df = pd.DataFrame([[1,2],[3,4]], columns =['a','b'])
df2 = pd.DataFrame([[5,6],[7,8]], columns =['a','b'])

df = df.append(df2)

print(df)
