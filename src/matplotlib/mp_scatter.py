import numpy as np
import matplotlib.pyplot as plt

#fixing random state for reproducibility
np.random.seed(19680801)

N = 50

x = np.random.rand(N)
y = np.random.rand(N)

colors = np.random.rand(N)

area = (30* np.random.rand(N))**2 # 0 t0 15 point redii

plt.scatter(x,y,s=area,c=colors,alpha=0.5)
plt.show()
