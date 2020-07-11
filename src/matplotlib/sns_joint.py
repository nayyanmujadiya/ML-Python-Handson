import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sample_super_store=pd.read_excel('Sample - Superstore.xls')

jp1 = sns.jointplot(data=sample_super_store,x='Sales',y='Profit')


