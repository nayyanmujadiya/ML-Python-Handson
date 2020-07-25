#you will need..
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cancer_sur = pd.read_csv("haberman.csv")

print(cancer_sur.head())

'''
header = None removes its headers, names =[] adds column names to the dataset as “Age”, “Operation_year, “axil_nodes_det”, “Surv_status”.
'''


cancer_sur = pd.read_csv("haberman.csv", header = None, names = ["Age", "Operation_year", "axil_nodes_det", "Surv_status"])

#print(cancer_sur.head())
#print(cancer_sur.tail())

'''
u can see count(gives total rows),Mean(average),std(standard deviation from one point to another),min,max and total coulmns of dataset and its rows, its data types by using .describe() and .info().
'''

#print(cancer_sur.describe())
#print(cancer_sur.info())

'''
.shape gives no of rows and columns.
'''
#print(cancer_sur.shape)

'''
Surv_status is a target column where it gives 2 values 1(means survived) and 2(not survived). lets see them. in the entire dataset we have 225 rows(people) with value 1(survived) and 81rows(people) with value 2(not survived).
'''
#print(cancer_sur["Surv_status"].value_counts())

'''
distribution plots
we draw this using seaborn as sns, Facetgrid gives grid layout, Cancer_sur is variable that we loaded data into.Hue colors the value/columnname that you give to it. Size is graph size and mapping all these to sns.distplot on “Age” column.
'''
#sns.FacetGrid(cancer_sur, hue = "Surv_status", height = 5).map(sns.distplot,"Age").add_legend()
#plt.show()

'''
from the above graph, you can observe that people with age 50 to 60 have more survival rate.
'''

'''
now lets draw the same with another column “Operation_year”
'''
#sns.FacetGrid(cancer_sur, hue = "Surv_status", height = 5).map(sns.distplot,"Operation_year").add_legend()
#plt.show()

'''
from the above graph we can say that people who had operation in the year from 58 to 66 had more survival rate.
'''
'''
counts, bin_edges = np.histogram(cancer_sur['Age'], bins=10, density = True)
plt.xlabel('Age')
pdf = counts/(sum(counts))
print("pdf=",pdf)
print("bin_edges=",bin_edges)
cdf = np.cumsum(pdf)
print("cdf=",cdf)
plt.plot(bin_edges[1:],pdf)
plt.plot(bin_edges[1:], cdf)
plt.show()
'''

'''
if we draw a straight line from Age value at 70, then it intersects the curve Cummulative distribution funtion(yellow) at value approximately equal to 0.8 i.e there are 80% people from cummulative sum of 30 to 70 age.
'''

'''
boxplot
'''

#sns.boxplot(x='Surv_status', y='Age', data=cancer_sur)
#plt.show()

'''
Now lets draw the Box plot between Surv_Status and Operation year.
it is observed that people that had operation in year 1958 to 1966 survived.
'''
#sns.boxplot(x='Surv_status', y='Operation_year', data=cancer_sur)
#plt.show()

'''
Voilin plot
'''
#sns.violinplot(x='Surv_status', y='Operation_year', data=cancer_sur, size=8)
#plt.show()

'''
pair plot
'''
#sns.pairplot(cancer_sur,hue="Surv_status",height=3)
#plt.show()
