import pandas as pd
import numpy as np

'''
Merge or join operations
combine datasets by linking rows using one or more
keys . These operations are central to relational
databases (e.g., SQL-based). The merge function in pandas is the main entry point for using these
algorithms on your data.

Let’s start with a simple example:
'''

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
print(df1)
print(df2)

'''
This is an example of a many-to-one join; the data in
df1 has multiple rows labeled
a and b , whereas df2 has only one row for each value in the
key column. Calling merge with these objects we obtain:
'''

pd.merge(df1, df2)

'''
Note that I didn’t specify which column to join on. If that information is not
specified, merge uses the overlapping
column names as the keys. It’s a good practice to specify explicitly,
though:
'''

pd.merge(df1, df2, on='key')

'''
If the column names are different in each object, you can specify
them separately:
'''


df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})

df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})

pd.merge(df3, df4, left_on='lkey', right_on='rkey')


'''
You may notice that the 'c' and
'd' values and associated data are
missing from the result. By default merge does an 'inner' join; the keys in the result are the
intersection, or the common set found in both tables. Other possible
options are 'left' , 'right' , and 'outer' . The outer join takes the union of the
keys, combining the effect of applying both left and right joins:
'''

pd.merge(df1, df2, how='outer')

'''
Many-to-many merges have well-defined, though not necessarily intuitive,
behavior. Here’s an example:
'''

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})
df1
df2
pd.merge(df1, df2, on='key', how='left')

'''
Many-to-many joins form the Cartesian product of the rows. Since there were three
'b' rows in the left DataFrame and
two in the

right one, there are six 'b' rows in the result.
'''

'''

The join method only
affects the distinct key values appearing in the result:

'''

pd.merge(df1, df2, how='inner')


'''
To merge with multiple keys, pass a list of column names:
'''

left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})

right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})

pd.merge(left, right, on=['key1', 'key2'], how='outer')


'''
A last issue to consider in merge operations is the treatment of
overlapping column names. While you can address the overlap manually
(see on renaming axis labels), merge has a suffixes option for specifying strings to
append to overlapping
names in the left and right DataFrame
objects:
'''

pd.merge(left, right, on='key1')

pd.merge(left, right, on='key1', suffixes=('_left', '_right'))
