from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

fig, axes = plt.subplots(1,3, figsize=(20,4), dpi=100)
pd.read_csv('https://raw.githubusercontent.com/nayyanmujadiya/ML-Python-Handson/master/dataset/ts/guinearice.csv', parse_dates=['date'], index_col='date').plot(title='Trend Only', legend=False, ax=axes[0])
#plt.show()
pd.read_csv('https://raw.githubusercontent.com/nayyanmujadiya/ML-Python-Handson/master/dataset/ts/sunspotarea.csv', parse_dates=['date'], index_col='date').plot(title='Seasonality Only', legend=False, ax=axes[1])

#plt.show()

pd.read_csv('https://raw.githubusercontent.com/nayyanmujadiya/ML-Python-Handson/master/dataset/ts/AirPassengers.csv', parse_dates=['date'], index_col='date').plot(title='Trend and Seasonality', legend=False, ax=axes[2])
plt.show()
