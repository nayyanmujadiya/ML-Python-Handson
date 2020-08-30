'''
download dataset from
https://www.kaggle.com/uciml/breast-cancer-wisconsin-data
'''

'''
Step 1: Load Pandas library and the dataset using Pandas
'''

import pandas as pd
dataset = pd.read_csv('Cancer_data.csv')

X = pd.DataFrame(dataset.iloc[:,:-1])
y = pd.DataFrame(dataset.iloc[:,-1])

print(X)
print(y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.20)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=20, criterion='gini',random_state=1,max_depth=3)
classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test,y_pred))

import pandas as pd
feature_imp = pd.Series(classifier.feature_importances_,index=X.columns).sort_values(ascending=False)
print(feature_imp)


import matplotlib.pyplot as plt
import seaborn as sns
sns.barplot(x=feature_imp, y=feature_imp.index)
plt.xlabel('Feature Importance Score')
plt.ylabel('Features')
plt.title('Visualizing Important Features')
#plt.show()

'''
Now let us see how the ‘SelectFromModel’ function helps in building a random forest classifier model with important features.
'''

from sklearn.feature_selection import SelectFromModel

feat_sel = SelectFromModel(classifier,threshold=0.1)
feat_sel.fit(X_train,y_train)

X_imp_train = feat_sel.transform(X_train)
X_imp_test = feat_sel.transform(X_test)

'''
Let us now build a new random forest classifier model (so that we can compare the results of this model with the old one)
'''

clf_imp = RandomForestClassifier(n_estimators=20, criterion='gini',random_state=1,max_depth=7)

clf_imp.fit(X_imp_train,y_train)

y_pred = classifier.predict(X_test)
print(accuracy_score(y_test,y_pred))

y_imp_pred = clf_imp.predict(X_imp_test)
print(accuracy_score(y_test,y_imp_pred))


'''
Note: After the feature selection process, the accuracy score is decreased. But, we have successfully picked out the important features at a small cost of accuracy.

Also, automatic feature selection reduces the complexity of the model but does not necessarily increase the accuracy. In order to get the desired accuracy, we have to perform the feature selection process manually.
'''
