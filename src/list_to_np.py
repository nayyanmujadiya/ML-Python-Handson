#this is NumPy example
import numpy as np
import matplotlib.pyplot as plt

cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]

C = np.array(cvalues)

print(C)

#Let's assume, we want to turn the values into degrees Fahrenheit.

print(C * 9 / 5 + 32)

print(C)
print(type(C))
#pure python implementation
fvalues = [ x*9/5 + 32 for x in cvalues]
print(fvalues)

plt.plot(C)
plt.show()
