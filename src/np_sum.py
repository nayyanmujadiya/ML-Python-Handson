import numpy as np
import pandas as pd

np_array_2d = np.arange(0, 6).reshape([2,3])

print(np_array_2d)

np.sum(np_array_2d, axis = 0)

np.sum(np_array_2d, axis = 1)

np_array_1s = np.array([[1,1,1],[1,1,1]])
np_array_9s = np.array([[9,9,9],[9,9,9]])

np.concatenate([np_array_1s, np_array_9s], axis = 0)

np.concatenate([np_array_1s, np_array_9s], axis = 1)

#let's see DataFrame
df = pd.DataFrame({"x":[1,2,3,4,5],
                   "y":[3,4,5,6,7]})

print(df)

print(df.mean(axis=0))

print(df.mean(axis=1))
