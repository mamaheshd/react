# Series and dataFrame are two widely used data structure of pandas.

import pandas as pd 
d=pd.Series([4,7,-5,3])
print(d)
print(d[1])
d[2]=8 # modify the value at index 2
print(d)
print(d.values)

# label
d=pd.Series([4,7,-5,3],index=['a','b','c','d',])
print(d)
print(d['a'])

# scalar multiplication
d=d*2
print(d)

#checking for null values
print(pd.isnull(d))
print(pd.notnull(d))

# DataFrame it represent tabular, spreadsheet like data structure containing an ordered collection of colums, each of can be a different data types
data={'State':['Bagmati','Koshi','Gandaki','Lumbini','Karnali'], 'Year':[2000,2001,2005,2005,20001]}
frame1=pd.DataFrame(data)
print(frame1)


