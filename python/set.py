# set: unorder collection of unique value
x={1,2,1,2,30,10,20}
print(x)
print(len(x))
print(type(x))
x.add(400)
print(x)

y=set(('a','b','c','d'))
print(y)
#update()
x.update(y)
print(x)

#discard()
y.discard('d')
print(y)

x.pop()
print(x)

a={1,2,3,4,5,6}
b={5,6,7,8,9}

c=a.difference(b)
print(c)

d=a.intersection(b)
print(d)


