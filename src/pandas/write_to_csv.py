import pandas as pd
import sys
import numpy as np
data = pd.read_csv('ex5.csv')
#print(data)

#data.to_csv('out1.csv')
#!cat examples/out.csv

'''
Other delimiters can be used, of course (writing to sys.stdout so it
prints the text result to the console):
'''

data.to_csv(sys.stdout, sep='|')

'''
Missing values appear as empty strings in the output. You might
want to denote them by some other sentinel value:
'''
data.to_csv(sys.stdout, na_rep='NULL')

'''
With no other options specified, both the row and column labels
are written. Both of these can be disabled:
'''

data.to_csv(sys.stdout, index=False, header=False)

'''
You can also write only a subset of the columns, and in an order
of your choosing:
'''

data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])

'''
Series also has a to_csv method:
'''
dates = pd.date_range('1/1/2000', periods=7)
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv('tseries.csv')
#!cat examples/tseries.csv
