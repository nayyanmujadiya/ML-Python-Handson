import numpy as np

arr = np.random.randn(5, 4)
print(arr)
arr.mean()
np.mean(arr)
arr.sum()

#arr.mean(axis=1)
#print(arr.sum(axis=0))

'''
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
arr.cumsum()

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
arr
arr.cumsum(axis=0)
arr.cumprod(axis=1)
'''
