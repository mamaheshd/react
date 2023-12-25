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

fruits1=['apple','cherry','papaya','kiwi']
fruits1.remove('apple')
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
