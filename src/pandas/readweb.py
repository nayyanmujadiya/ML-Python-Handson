'''
To find the last 30 GitHub issues for pandas on GitHub, we can
make a GET HTTP request
using the add-on requests library:
'''
import pandas as pd
import requests

'''
The Response object’s json method
will return a dictionary containing JSON parsed into native
Python objects:
'''

url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
#print(resp)

data = resp.json()
print(data[0]['title'])
print(data[1]['title'])

'''
Each element in data is a
dictionary containing all of the data found on a GitHub issue page (except
for the comments). We can pass data directly to DataFrame and extract fields of interest:
'''

issues = pd.DataFrame(data, columns=['number', 'title',
                                     'labels', 'state'])
#print(issues)
