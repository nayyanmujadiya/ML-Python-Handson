import pandas as pd

tables = pd.read_html('fdic_failed_bank_list.html')
len(tables)
failures = tables[0]
failures.head()

'''
from here we could proceed to
do some data cleaning and analysis, like computing the number of bank
failures by year:
'''

close_timestamps = pd.to_datetime(failures['Closing Date'])
close_timestamps.dt.year.value_counts()
