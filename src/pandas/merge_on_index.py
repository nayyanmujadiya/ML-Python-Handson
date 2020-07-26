import pandas as pd
import numpy as np

'''
In some cases, the merge key(s) in a DataFrame will be found in its index. In this case, you
can pass left_index=True or right_index=True (or both) to indicate that
the index should be used as the merge key:
'''

left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

left1

right1

pd.merge(left1, right1, left_on='key', right_index=True)

'''
Since the default merge method is to intersect the join keys, you
can instead form the union of them with an outer join:
'''

pd.merge(left1, right1, left_on='key', right_index=True, how='outer')


'''
With hierarchically indexed data, things are more complicated, as
joining on index is implicitly a multiple-key merge:
'''

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio',
                               'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})

righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio',
                              'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])

lefth

righth

'''
In this case, you have to indicate multiple columns to merge on as
a list (note the handling of duplicate index values with
how='outer' ):
'''

pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)

pd.merge(lefth, righth, left_on=['key1', 'key2'],
         right_index=True, how='outer')


'''
Using the indexes of both sides of the merge is also
possible:
'''

left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=['a', 'c', 'e'],
                     columns=['Ohio', 'Nevada'])

right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=['b', 'c', 'd', 'e'],
                      columns=['Missouri', 'Alabama'])

left2

right2

pd.merge(left2, right2, how='outer', left_index=True, right_index=True)

'''
DataFrame has a convenient join instance
for merging by index. It can also be used to combine together
many DataFrame objects having the same or similar indexes but
non-overlapping columns. In the prior example, we could have
written:
'''

left2.join(right2, how='outer')

'''
In part for legacy reasons (i.e., much earlier versions of
pandas), DataFrame’s join method
performs a left join on the join keys, exactly preserving the left
frame’s row index. It also supports joining the index of the passed
DataFrame on one of the columns of
the calling DataFrame:
'''

left1.join(right1, on='key')

'''
Lastly, for simple index-on-index merges, you can pass a list of
DataFrames to join as an alternative
to using the more general concat function described in the next section :
'''

another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                       index=['a', 'c', 'e', 'f'],
                       columns=['New York', 'Oregon'])

another

left2.join([right2, another])

left2.join([right2, another], how='outer')
