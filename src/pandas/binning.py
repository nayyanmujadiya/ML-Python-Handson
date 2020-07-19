import pandas as pd

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

'''
Let’s divide these into bins of 18 to 25, 26 to 35,
36 to 60, and
finally 61 and older.
To do so, you have to use cut , a function in pandas:
'''

bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
cats

'''
The object pandas returns is a special Categorical object. The output you see describes the bins computed by
pandas.cut . You can treat it like an array of strings
indicating the bin name; internally it contains a categories array specifying the distinct
category names along with a labeling for the ages data in the codes attribute:
'''
cats.codes
cats.categories
pd.value_counts(cats)

'''
Note that pd.value_counts(cats) are the bin counts for the result of
pandas.cut . Consistent with mathematical notation for intervals, a parenthesis
means that the side is open , while the square
bracket means it is closed (inclusive). You can change which side
is closed by passing right=False :
'''

pd.cut(ages, [18, 26, 36, 61, 100], right=False)

'''
You can also pass your own bin names by passing a list or array to
the labels option:
'''

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
pd.cut(ages, bins, labels=group_names)

'''
If you pass an integer number of bins to cut instead of explicit bin edges, it will compute
equal-length bins based on the minimum and maximum values in the data.
Consider the case of some uniformly distributed data chopped into
fourths:
'''

data = np.random.rand(20)
pd.cut(data, 4, precision=2)

'''
A closely related function, qcut , bins the data based on sample quantiles. Depending on the
distribution of the data, using cut will not usually result in each bin having the same number of data
points. Since qcut uses sample
quantiles instead, by definition you will obtain roughly equal-size
bins:
'''

data = np.random.randn(1000)  # Normally distributed
cats = pd.qcut(data, 4)  # Cut into quartiles
cats
pd.value_counts(cats)

'''
Similar to cut you can pass
your own quantiles (numbers between 0 and 1, inclusive):
'''

pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])
