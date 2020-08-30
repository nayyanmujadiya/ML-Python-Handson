'''
download dataset from
https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
'''

'''
Step 1: Load Pandas library and the dataset using Pandas
'''

import pandas as pd
dataset = pd.read_csv('Cancer_data.csv')
X = dataset.drop('Diagnosis',axis=1)
y = dataset['Diagnosis']

print(X)
print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.20)


'''
Step 4: Import the support vector classifier function or SVC function from Sklearn SVM module. Build the Support Vector Machine model with the help of the SVC function
'''
from sklearn.svm import SVC
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train,y_train)

'''
Step 5: Predict values using the SVM algorithm model
'''

y_pred = svclassifier.predict(X_test)

'''
Step 6: Evaluate the Support Vector Machine model
'''

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))


'''
Polynomial Kernel
'''

from sklearn.svm import SVC
svclassifier1 = SVC(kernel='poly', degree=6)
svclassifier1.fit(X_train,y_train)

y_pred1 = svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred1))
print(classification_report(y_test,y_pred1))

'''
Gaussian Kernel
'''
from sklearn.svm import SVC
svclassifier2 = SVC(kernel='rbf')
svclassifier2.fit(X_train,y_train)

y_pred2 = svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred2))
print(classification_report(y_test,y_pred2))

'''
Sigmoid Kernel
'''
from sklearn.svm import SVC
svclassifier3 = SVC(kernel='sigmoid')
svclassifier3.fit(X_train,y_train)

y_pred3 = svclassifier.predict(X_test)
print(confusion_matrix(y_test,y_pred3))
print(classification_report(y_test,y_pred3))



