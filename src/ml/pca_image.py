'''
PCA + Logistic Regression (MNIST)
The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.
'''

#from sklearn.datasets import fetch_mldata
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# You can add the parameter data_home to wherever to where you want to download your data
#mnist = fetch_mldata('MNIST original')
mnist = fetch_openml('mnist_784')

# These are the images
mnist.data.shape

# These are the labels
mnist.target.shape

#scaler = StandardScaler()

# Fit on training set only.
#mnist.data = scaler.fit_transform(mnist.data)

pca = PCA(.95)

lower_dimensional_data = pca.fit_transform(mnist.data)

print(pca.n_components_)

'''
The idea with going from 784 components to 154 is to reduce the running time of a supervised learning algorithm (in this case logistic regression) which we will see at the end of the tutorial. One of the cool things about PCA is that we can go from a compressed representation (154 components) back to an approximation of the original high dimensional data (784 components).
'''

approximation = pca.inverse_transform(lower_dimensional_data)

plt.figure(figsize=(8,4));

# Original Image
plt.subplot(1, 2, 1);
plt.imshow(mnist.data[1].reshape(28,28),
              cmap = plt.cm.gray, interpolation='nearest',
              clim=(0, 255));
plt.xlabel('784 components', fontsize = 14)
plt.title('Original Image', fontsize = 20);

# 154 principal components
plt.subplot(1, 2, 2);
plt.imshow(approximation[1].reshape(28, 28),
              cmap = plt.cm.gray, interpolation='nearest',
              clim=(0, 255));
plt.xlabel('154 components', fontsize = 14)
plt.title('95% of Explained Variance', fontsize = 20);
plt.show()

# if n_components is not set all components are kept (784 in this case)
pca = PCA()

pca.fit(mnist.data)

pca.n_components_


