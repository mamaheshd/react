# list is a collection data tyoeused in python . It is similar to array in other programming language. It is mutable ie element inside list can be changed ie remove or add or short. Element inside list are in the order and list allows duplicate values.
fruits=['apple','cherry','papaya','kiwi']
print(fruits)

#cout the no of element  in the list
print(len(fruits))
print(fruits[2])
print(fruits[-1])
print(fruits[2][2])

print(fruits[1:3])

# append() add new element in last in list 
fruits.append('orange')
print(fruits)

# pop() used to remove last element
fruits.pop()
print(fruits)

fruits.pop(1)
print(fruits)

fruits1=['apple','cherry','papaya','kiwi','lol']
# fruits1.remove('apple')
print(fruits1)

# clear() this method will empties the list
fruits2=['apple','cherry','papaya','kiwi']
fruits2.clear()
print(fruits2)

# del delete the list completely
num=[1,2,3,4]
del num 
# print(num)

test=list((1,2,3,4,2,3,5))
print(test)
x= list(range(10))
print(x)

y=list(range(1,10))
print(y)

z=list(range(1,20,2))
print(z)

nums=list(range(10,101,10))
print(nums)

# sort() 
fruits.sort() # ascending order
print(fruits)

fruits.sort(reverse=True) #descending order
print(fruits)

fruits1.reverse()
print(fruits)

# tuple-> similar to list but immutable ie element inside tuple cannot be changed and value are in the order and allow duplicate values
t=('apple','apple','cherry','papaya','kiwi','lol')
print(t)
print(len(t))
print(t[3])
print(t[-2])
print(t[1:5])
print(t[:5])

#count()
print(t.count('apple'))
print(t.count('orange'))


#index()
print(t.index('kiwi'))

a=list(t)
print(a)


#nested list
list1=[10,20,30,40,50]
list2=[1,2,3,4,5]
matrix=[list1,list2]
print(matrix)
print(matrix[0])
print(matrix[0][2])


