import pandas as pd

d = {'one': pd.Series([1,2,3], index=['a','b','c']),
     'tow': pd.Series([1,2,3,4], index=['a','b','c','d'])}

df = pd.DataFrame(d)
#print(df)
print (df['one'])

print("Adding a new column by passing as series:")

df['three'] = pd.Series([10,20,30],index=['a','b','c'])

print("Adding a new column using existing column")
#print(df)
df['four'] = df['one'] + df['three']
print(df)

#column deletion
del df['one']
print(df)

'''
del df['two']
print(df)
'''

