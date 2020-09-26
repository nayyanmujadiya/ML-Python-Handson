'''
https://in.springboard.com/blog/data-modelling-covid/
'''

import pandas as pd
#import plotly.graph_objects as go
import numpy as np

from dateutil.parser import parse
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.figsize': (10, 7), 'figure.dpi': 120})

confirmed_df = pd.read_csv("time_series_covid19_confirmed_global.csv")
print(confirmed_df)

death_df = pd.read_csv("time_series_covid19_deaths_global.csv")
print(death_df)

recovered_df = pd.read_csv("time_series_covid19_recovered_global.csv")
print(recovered_df)

cases_contry_df = pd.read_csv("cases_country.csv")
print(cases_contry_df)

print(confirmed_df.columns)

print(cases_contry_df.columns)

global_data = cases_contry_df.copy().drop(['Lat','Long_','Country_Region','Last_Update'],axis = 1)

global_summary = pd.DataFrame(global_data.sum()).transpose()

global_summary.style.format("{:,.0f}")

global_summary.to_csv("gd_sum.csv")
print(global_summary.columns)

print(global_summary)

'''
fig = go.Figure(data=go.Scatter())

fig.update_layout(title='Total Coronaviru Confirmed Case (Globally)', yaxis_title='Confirmed Cases',xaxis_tickangle = 315)
'''

confimed_agg_ts = confirmed_df.copy().drop(['Lat','Long','Country/Region','Province/State'],axis = 1).sum()
death_agg_ts = death_df.copy().drop(['Lat','Long','Country/Region',      'Province/State'],axis = 1).sum()
recovered_agg_ts = recovered_df.copy().drop(['Lat','Long','Country/Region',    'Province/State'],axis = 1).sum()
print(confimed_agg_ts.values)
active_agg_ts = pd.Series(data=np.array([x1-x2-x3 for (x1,x2,x3) in zip(confimed_agg_ts.values,death_agg_ts.values,recovered_agg_ts.values)]),index = confimed_agg_ts.index)


#active_agg_ts.to_csv("active_agg.csv")
#confimed_agg_ts.to_csv("confimed_agg.csv")
#death_agg_ts.to_csv("death_agg.csv")
#recovered_agg_ts.to_csv("recovered_agg.csv")
#import sys
#sys.exit()

a_df = pd.read_csv('active_agg.csv', parse_dates=['date'], index_col='date')
c_df = pd.read_csv('confimed_agg.csv', parse_dates=['date'], index_col='date')
d_df = pd.read_csv('death_agg.csv', parse_dates=['date'], index_col='date')
r_df = pd.read_csv('recovered_agg.csv', parse_dates=['date'], index_col='date')

# Draw Plot
def plot_df(df, x, y, title="", xlabel='Date', ylabel='Value', dpi=100):
    plt.figure(figsize=(16,5), dpi=dpi,)
    plt.plot(x, y, color='tab:red')
    plt.gca().set(title=title, xlabel=xlabel, ylabel=ylabel)

plot_df(a_df, x=a_df.index, y=a_df.value, title='covid')
plot_df(c_df, x=c_df.index, y=c_df.value, title='covid')
plot_df(d_df, x=d_df.index, y=d_df.value, title='covid')
plot_df(r_df, x=r_df.index, y=r_df.value, title='covid')
plt.show()
