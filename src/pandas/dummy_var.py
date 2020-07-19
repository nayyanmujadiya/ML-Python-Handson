import pandas as pd

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})

print(df)
pd.get_dummies(df['key'])

'''
In some cases, you may want to add a prefix to the columns in the
indicator DataFrame, which can
then be merged with the other data.
get_dummies has a prefix argument for
doing this:
'''

dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
df_with_dummy
