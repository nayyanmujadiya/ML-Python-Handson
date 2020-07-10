import numpy as np

arr = np.random.randn(100)
(arr > 0).sum() # Number of positive values

bools = np.array([False, False, True, False])
bools.any()
bools.all()
