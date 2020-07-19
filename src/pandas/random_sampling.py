import numpy as np
import pandas as pd

'''
Permuting (randomly reordering) a Series or the rows in a DataFrame is easy to do using the
numpy.random.permutation function.
Calling permutation with the length of the axis you want to permute produces an array of
integers indicating the new ordering:
'''

df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5)
sampler

'''
That array can then be used in iloc based indexing or the equivalent take function:
'''

df
df.take(sampler)

'''
To select a random subset without replacement,
you can use
the sample method on Series and
DataFrame:
'''

df.sample(n=3)

'''
To generate a sample with replacement (to
allow repeat choices), pass replace=True to
sample :
'''

choices = pd.Series([5, 7, -1, 6, 4])
draws = choices.sample(n=10, replace=True)
draws
