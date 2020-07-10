import numpy as np

arr = np.arange(10)
np.save('some_array', arr)

np.load('some_array.npy')

np.savez('array_archive.npz', a=arr, b=arr)

arch = np.load('array_archive.npz')
print(arch['b'])

np.savez_compressed('arrays_compressed.npz', a=arr, b=arr)
