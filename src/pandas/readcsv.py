import pandas as pd

df = pd.read_csv("ex1.csv")
#print(df)
#pd.read_table('ex1.csv', sep=',')

# not always have header
df = pd.read_csv("ex2.csv",header=None)
#print(df)

# you can give header name
df = pd.read_csv('ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
#print(df)

#which one is index
names = ['a', 'b', 'c', 'd', 'message']
df = pd.read_csv('ex2.csv', names=names, index_col='message')
#print(df)

'''
In the event that you want to form a hierarchical index from multiple columns, pass a list of column numbers or names:
'''
parsed = pd.read_csv('csv_mindex.csv',
                     index_col=['key1', 'key2'])
#print(parsed)

'''
In some cases, a table might not have a fixed delimiter, using
whitespace or some other pattern to separate fields. Consider a text file
that looks like this:
'''

#print(list(open('ex3.txt')))
'''
While you could do some munging by hand, the fields here are
separated by a variable amount of whitespace. In these cases, you can pass
a regular

expression as a delimiter for read_csv . This can be expressed by the regular
expression \s+ , so we have then:

Because there was one fewer column name than the number of data
rows, read_csv infers that the first
column should be the DataFrame’s index in this special case.

'''
result = pd.read_table('ex3.txt', sep='\s+')
#print(result)

'''
skip first, third, and fourth rows of a file with
'''

#!cat ex4.csv
df = pd.read_csv('ex4.csv', skiprows=[0, 2, 3])
#print(df)

'''
Handling missing values is an important and frequently nuanced part
of the file parsing process. Missing data is usually either not present
(empty string) or marked by some sentinel value.
By default, pandas uses a set of commonly occurring sentinels, such as
NA and NULL :
'''

#result = pd.read_csv('ex5.csv')
#result = pd.read_csv('examples/ex5.csv')
#print(result)
#print(pd.isnull(result))

'''
The na_values option can take
either a list or set of strings to consider missing values :
'''
result = pd.read_csv('ex5.csv', na_values=['NULL'])
print(result)

'''
Different NA sentinels can be specified for each column in a
dict:
'''
sentinels = {'message': ['foo','NA'], 'something': ['two']}
r = pd.read_csv('ex5.csv', na_values=sentinels)
#print(r)
