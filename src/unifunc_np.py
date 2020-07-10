import numpy as np

#sqrt and exp e^x
arr = np.arange(10)
print(arr)
print(np.sqrt(arr))
print(np.exp(arr))

# maximum
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)
print(np.maximum(x, y))

'''
return fractional and integral parts of
'''
arr = np.random.randn(7) * 5
print(arr)
remainder, whole_part = np.modf(arr)
print(remainder)
print(whole_part)

print(arr)
np.sqrt(arr)
#np.sqrt(arr, arr)
print(arr)
