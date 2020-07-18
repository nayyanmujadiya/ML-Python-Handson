import pandas as pd

pd.options.display.max_rows = 10

result = pd.read_csv('ex6.csv')
#print(result)

'''
If you want to only read a small number of rows (avoiding reading
the entire file), specify that with nrows :
'''

nr = pd.read_csv('ex6.csv', nrows=5)
#print(nr)

'''
To read a file in pieces, specify a chunksize as a number of rows:
'''
chunker = pd.read_csv('ex6.csv', chunksize=1000)
#print(chunker)

'''
The TextFileReader object
returned by read_csv allows you to iterate over the parts of the file according to the
chunksize . For example, we can
iterate over ex6.csv , aggregating the
value counts in the 'key' column like
so:
'''

chunker = pd.read_csv('ex6.csv', chunksize=1000)

tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)

#print(tot[:10])

'''
TextParser is also equipped
with a get_chunk method that enables you to read pieces of an arbitrary size.
'''
