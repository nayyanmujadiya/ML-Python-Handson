'''
We will replace the values NN and LN of the following DataFrame in different ways by using the parameter method.
'''
import pandas as pd

df = pd.DataFrame({
    'name':['Ben', 'Kate', 'Agnes', 'Ashleigh', 'Tom'],
    'job':['programmer', 'NN', 'NN', 'engineer', 'teacher'],
    'language':['Java', 'Python', 'LN', 'LN', 'C']})

'''
Every occurrence of NN in the job column will have to be replaced. The value is defined by the parameter method. ffill means 'forward fill', i.e. we will take the preceding value to the first NN as the fill value. This is why we will replace the values by 'programmer':
'''

df.replace(to_replace='NN',
           value=None,
           method='ffill')
'''
what happens, if we use bfill (backward fill). Now the occurrences of 'LN' become 'C' instead of Python. We also turn the 'NN's into engineers instead of programmers.
'''
df.replace(to_replace='NN',
           value=None,
           method='bfill')

'''
pad and ffill are same
pad is default for method
'''
