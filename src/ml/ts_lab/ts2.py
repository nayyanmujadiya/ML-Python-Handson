
from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})


# dataset source: https://github.com/rouseguy
df = pd.read_csv('https://raw.githubusercontent.com/nayyanmujadiya/ML-Python-Handson/master/dataset/ts/MarketArrivals.csv')
df = df.loc[df.market=='MUMBAI', :]
print(df.head())
