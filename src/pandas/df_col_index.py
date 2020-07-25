import pandas as pd
import numpy as np

frame = pd.DataFrame({'a': range(7), 'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two',
                            'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})
print(frame)

'''
DataFrame’s set_index function
will create a new DataFrame using one or more of its columns as the
index:
'''

frame2 = frame.set_index(['c', 'd'])
print(frame2)

'''
By default the columns are removed from the DataFrame, though you
can leave them in:
'''

frame.set_index(['c', 'd'], drop=False)

'''
reset_index , on the other hand,
does the opposite of set_index ; the
hierarchical index levels are moved into the columns:
'''

frame2.reset_index()
