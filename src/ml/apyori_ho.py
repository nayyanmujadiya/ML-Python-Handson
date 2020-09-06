import numpy as np
import pandas as pd
from apyori import apriori

store_data = pd.read_csv("Day1.csv",header=None)

print(store_data)

print(store_data.shape)

records = []

for i in range(0,22):
    records.append([str(store_data.values[i,j]) for j in range(0,6)])


association_rules = apriori(records,min_support=0.50,min_confidence=0.7,min_lift=1.2,min_length=2)

association_results = list(association_rules)

print(len(association_results))

print(association_results)
