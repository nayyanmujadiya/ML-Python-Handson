from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse
from statsmodels.tsa.stattools import adfuller, kpss

# Import Data
df = pd.read_csv('https://raw.githubusercontent.com/nayyanmujadiya/ML-Python-Handson/master/dataset/ts/a10.csv', parse_dates=['date'])

# Using scipy: Subtract the line of best fit
from scipy import signal

df = pd.read_csv('https://raw.githubusercontent.com/nayyanmujadiya/ML-Python-Handson/master/dataset/ts/a10.csv', parse_dates=['date'])
detrended = signal.detrend(df.value.values)
plt.plot(detrended)
plt.title('Drug Sales detrended by subtracting the least squares fit', fontsize=16)
plt.show()

# Using statmodels: Subtracting the Trend Component.
from statsmodels.tsa.seasonal import seasonal_decompose

df = pd.read_csv('https://raw.githubusercontent.com/nayyanmujadiya/ML-Python-Handson/master/dataset/ts/a10.csv', parse_dates=['date'],index_col='date')
result_mul = seasonal_decompose(df['value'], model='multiplicative', extrapolate_trend='freq')
detrended = df.value.values - result_mul.trend
plt.plot(detrended)
plt.title('Drug Sales detrended by subtracting the trend component', fontsize=16)
plt.show()
