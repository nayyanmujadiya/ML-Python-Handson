import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

tips=sns.load_dataset("tips")

ax=sns.boxplot(x="day",y=tips["total_bill"],data=tips)

