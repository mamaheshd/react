# numpy-> numerical python 
import numpy as np
data=[[1,2,6],[3,7,9]]
d=np.array(data)
print(d)
print(d.shape)

# check data type of array element
print(d.dtype)
print(type(d))

#one dimensional array
x=(10,12,15)
x=np.array(x)
print(x)

# we can specify data type of array element explicitly using dtype
data=np.array([1,2,5,7],dtype='int64')
print(data)
print(data.dtype)

# create array of length 5 using zeros()
a=np.zeros(5)
print(a)

a=np.ones(5)
print(a)

z=np.empty((2,3))
print(z)

#arnge()
c=np.arange(10)
print(c)
