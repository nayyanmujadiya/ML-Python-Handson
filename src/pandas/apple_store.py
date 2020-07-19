# import the libraries
import numpy as np
import pandas as pd
import sys

# import the dataset
df = pd.read_csv('Social_Network_Ads.csv')

print(df['Purchased'].value_counts())
#print(df.head(30))
#sys.exit("Test")
# get dummy variables
df_getdummy=pd.get_dummies(data=df, columns=['Gender'])

# seperate X and y variables
X = df_getdummy.drop('Purchased',axis=1)
y = df_getdummy['Purchased']
