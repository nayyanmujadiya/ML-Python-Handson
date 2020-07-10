import numpy as np

# Generate some random data
data = np.random.randn(2,3)

print(data)

# multi with each cell
print(data * 10)

# add each cell
print(data + data)

#shape
print(data.shape)

#ndim
print(data.ndim)

#size
print(data.size)

#type
print(data.dtype)
