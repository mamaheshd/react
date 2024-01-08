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

r=np.array([[1.,2.,3.],[4.,5.,6.]])
print(r)

# element wise multiplication
result=r*r
print(result)

#element wise addition
result=r+r
print(result)

c=np.arange(1,10)
print(c[4]) #indexing
print(c[3:8]) #slicing

#boolean indexing
a=np.array([12,24,16,27,30,40,43,7])
boolean_mask=a>20
print(a[boolean_mask])

#fancy indexing
fancy_indexing=a[[1,4,5]]
print(fancy_indexing)

# unary  universal function 
a=np.arange(10)
s=np.sqrt(a)
print(s)

#linear algebra
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[6,12],[1,5],[8,9]])
#matrix multiplication
result=x.dot(y)
print(result)
r=np.dot(x,y)
print(r)

# transpose
r=np.transpose(x)
print(r)