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
frame2=pd.DataFrame(data,columns=['State','Year','Dept'])
print(frame2)
print(frame2['State'])
obj=pd.Series([2,3,3,4,5])
frame2['Dept']=obj
print(frame2)

# covariance
d=pd.DataFrame({
    'A':[5,3,6,4],
    'B':[11,2,4,3],
    'C':[6,4,8,5],
    'D':[3,4,3,5]
})
print(d)
print(d.cov())
print(d.corr()) #corelation

# handling missing values
#dropna,fillna,isnull,notnull
import numpy as np
s=pd.Series(['a','b',np.nan,'c',np.nan])
print(s)
print(s.isnull())
s1=s.dropna()
print(s1)
s2=s.fillna(0)
print(s2)

