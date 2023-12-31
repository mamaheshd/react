#zip() to quickly create a list of tuple by zipping up together two list
list1=[1,2,3,4]
list2=['a','b','c','d','e','f']
result=list(zip(list1,list2))
print(result)

#min and max
print(min([1,2,4,5,-8]))

print(max([1,2,4,5,-8]))


#random
from random import shuffle
list=[1,2,3,4,5,6,7,9]
shuffle(list)
print(list)

from random import randint
y=randint(1,10)
print(y)