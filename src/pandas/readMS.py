import pandas as pd

'''
To use ExcelFile , create an
instance by passing a path to an xls or xlsx file:
'''
xlsx = pd.ExcelFile('ex1.xlsx')

'''
Data stored in a sheet can then be read into DataFrame with parse :
'''
pd.read_excel(xlsx, 'Sheet1')

'''
If you are reading multiple sheets in a file, then it
is faster to
create the ExcelFile , but you can also simply pass
the filename to pandas.read_excel :
'''
frame = pd.read_excel('ex1.xlsx', 'Sheet1')
frame

'''
To write pandas data to Excel format, you must first create an
ExcelWriter , then write data to it using
pandas objects’ to_excel method:
'''
writer = pd.ExcelWriter('ex2.xlsx')
frame.to_excel(writer, 'Sheet1')
writer.save()

'''
You can also pass a file path to to_excel and
avoid the ExcelWriter :
'''
frame.to_excel('ex2.xlsx')

#!rm ex2.xlsx
