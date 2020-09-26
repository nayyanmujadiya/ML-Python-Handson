'''
https://in.springboard.com/blog/data-modelling-covid/
'''

import pandas as pd


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
