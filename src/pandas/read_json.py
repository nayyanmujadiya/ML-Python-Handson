import pandas as pd
import json
obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
              {"name": "Katie", "age": 38,
               "pets": ["Sixes", "Stache", "Cisco"]}]
}
"""

result = json.loads(obj)
print(result)

'''
json.dumps , on the other hand, converts a Python object back to JSON:
'''
asjson = json.dumps(result)

'''
How you convert a JSON object or list of objects to a DataFrame or
some other data structure for analysis will be up to you. Conveniently,
you can pass a list of dicts (which were previously JSON objects) to the
DataFrame constructor and select a subset of the data fields:
'''

siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
print(siblings)

'''
The pandas.read_json can automatically convert JSON datasets in specific
arrangements into a Series or DataFrame. For example:
'''
'''
The default options for pandas.read_json assume
that each object in the JSON array is a row in the table:
'''
data = pd.read_json('example.json')
print(data)

'''
If you need to export data from pandas to JSON, one way is to use
the to_json methods on Series and DataFrame
'''
print(data.to_json())
print(data.to_json(orient='records'))
