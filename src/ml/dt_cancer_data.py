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

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion='gini',random_state=100,max_depth=None,min_samples_leaf=1)
classifier.fit(X_train,y_train)

from sklearn.tree import export_graphviz
import pydotplus
export_graphviz(classifier,out_file='clf_tree.dot')

'''
After executing this step, the ‘clf_tree.dot’ file will be saved in your system. Now to visualize the tree, open this file with the ‘.dot’ extension and copy the graphviz data. Then, go to the site ‘http://www.webgraphviz.com/’ and paste the graphviz data there
'''

'''
After this step, let us perform the decision tree analysis now.
'''

y_pred = classifier.predict(X_test)

print(y_pred)
print(y_test)

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
