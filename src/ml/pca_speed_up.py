'''
PCA + Logistic Regression (MNIST)
'''
from sklearn.datasets import fetch_openml
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.model_selection import train_test_split
import pandas as pd

# You can add the parameter data_home to wherever to where you want to download your data
mnist = fetch_openml('mnist_784')

#print(mnist)

# These are the images
print(mnist.data.shape)

# These are the labels
print(mnist.target.shape)

# test_size: what proportion of original data is used for test set
train_img, test_img, train_lbl, test_lbl = train_test_split(
    mnist.data, mnist.target, test_size=1/7.0, random_state=0)

print(train_img.shape)

print(train_lbl.shape)

print(test_img.shape)

print(test_lbl.shape)

'''
Standardizing the Data¶
Since PCA yields a feature subspace that maximizes the variance along the axes, it makes sense to standardize the data, especially, if it was measured on different scales.

Standardization of a dataset is a common requirement for many machine learning estimators: they might behave badly if the individual feature do not more or less look like standard normally distributed data
'''

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Fit on training set only.
scaler.fit(train_img)

# Apply transform to both the training set and the test set.
train_img = scaler.transform(train_img)
test_img = scaler.transform(test_img)

'''
PCA to Speed up Machine Learning Algorithms (Logistic Regression)
'''

'''
Import and use PCA. After PCA you will apply a machine learning algorithm of your choice to the transformed data
'''

from sklearn.decomposition import PCA

pca = PCA(.95)

pca.fit(train_img)

print(pca.n_components_)

train_img = pca.transform(train_img)
test_img = pca.transform(test_img)

from sklearn.linear_model import LogisticRegression

# all parameters not specified are set to their defaults
# default solver is incredibly slow thats why we change it
# solver = 'lbfgs'
logisticRegr = LogisticRegression(solver = 'lbfgs')

logisticRegr.fit(train_img, train_lbl)

# Returns a NumPy Array
# Predict for One Observation (image)
logisticRegr.predict(test_img[0].reshape(1,-1))

# Predict for Multiple Observations (images) at Once
logisticRegr.predict(test_img[0:10])

score = logisticRegr.score(test_img, test_lbl)
print(score)
