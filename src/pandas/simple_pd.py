import pandas as pd

obj = pd.Series([4, 7, -5, 3])

print(obj)

print(obj.values)
print(obj.index)  # like range(4)

'''
print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)
'''

