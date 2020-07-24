import pandas as pd
import numpy as np
#makes the random numbers predictable
np.random.seed(0)
factors = np.random.randn(30)
'''
we specified five bins in out example, so we are asking qcut for quintiles.

'''

'''
So, when we ask for quintiles with qcut, the bins will be chosen so that we have the same number of records in each bin. we have 30 records, so should have 6 in each bin (output should look like this, although the breakpoints will differ due to the random draw):
'''
print(pd.qcut(factors, 5).value_counts())

'''
Conversely, for cut you will see something more uneven:
That's because cut will choose the bins to be evenly spaced according to the values themselves and not the frequency of those values. Hence, because you drew from a random normal, you'll see higher frequencies in the inner bins and fewer in the outer. This is essentially going to be a tabular form of a histogram (which you would expect to be fairly bell shaped with 30 records).
'''
print(pd.cut(factors, 5).value_counts())
