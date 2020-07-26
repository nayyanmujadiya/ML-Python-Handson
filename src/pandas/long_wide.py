import pandas as pd
import numpy as np

data = pd.read_csv('examples/macrodata.csv')

data.head()

'''
We will look at PeriodIndex a bit more closely
in Time series
'''
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter,
                         name='date')

columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')

data = data.reindex(columns=columns)

data.index = periods.to_timestamp('D', 'end')

ldata = data.stack().reset_index().rename(columns={0: 'value'})


'''
In short, it combines the
year and quarter columns to create
a kind of time interval type.
'''

ldata[:10]

'''
This is the so-called long format for
multiple time series, or other observational data with two or more keys
(here, our keys are date and item). Each row in the table represents a
single observation.
'''

'''
Data is frequently stored this way in relational databases like MySQL, as a fixed schema (column names and
data types)

allows the number of distinct values in the item column to change as data is added to the
table. In the previous example, date and item would usually be the primary
keys (in relational database parlance), offering both relational
integrity and easier joins. In some cases, the data may be more
difficult to work with in this format; you might prefer to have a
DataFrame containing one column per distinct item value indexed by timestamps in the
date column. DataFrame’s pivot method performs exactly this transformation:
'''

pivoted = ldata.pivot('date', 'item', 'value')

pivoted

'''
The first two values passed are the columns to
be used
respectively as the row and column index, then finally an optional value
column to fill the DataFrame.
'''

'''
Suppose you had two value columns that you
wanted to reshape simultaneously:
'''
ldata['value2'] = np.random.randn(len(ldata))

ldata[:10]

'''
By omitting the last argument, you obtain a DataFrame with
hierarchical columns:
'''

pivoted = ldata.pivot('date', 'item')

pivoted[:5]

pivoted['value'][:5]

'''
Note that pivot is equivalent
to creating a hierarchical index using set_index followed by a call to unstack :
'''

unstacked = ldata.set_index(['date', 'item']).unstack('item')

unstacked[:7]
