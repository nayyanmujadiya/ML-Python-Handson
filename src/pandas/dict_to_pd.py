import pandas as pd
#dict is given
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
print(obj3)

'''
When you are only passing a dict, the index in the resulting Series will
have the dict’s keys in sorted order. You can override this by passing
the dict keys in the order you want them to appear in the resulting
Series:
'''

states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)

'''
no value for California
'''
#to detect missing data
print(pd.isnull(obj4))
print(pd.notnull(obj4))

# on instance
obj4.isnull()
'''
I discuss working with missing data in more detail in class.
'''

# Arithmetic operations
print(obj3)
print(obj4)
print(obj3 + obj4)
'''
Data alignment features will be addressed in more detail later. If
you have experience with databases, you can think about this as being
similar to a join operation.
'''
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)
