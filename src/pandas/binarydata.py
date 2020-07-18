import pandas as pd

frame = pd.read_csv('ex1.csv')
print(frame)
frame.to_pickle('frame_pickle')

'''
You can read any “pickled” object stored in a file by using the
built-in pickle directly, or even more conveniently
using pandas.read_pickle :
'''
df = pd.read_pickle('frame_pickle')
print(df)
#!rm frame_pickle
