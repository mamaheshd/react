students={
    'name':'Mahesh',
    'age':24,
    'gender':'male'
}
print(students)
print(students['name'])

d={}
d['name']='lushi'
d['age']=24
print(d)

d.update({'age':'23'})
print(d)

d.pop('age')
print(d)

# keys() it only print all the keys of the dictionary
print(students.keys())
print(students.values())

#nested dictionary
test={'key1':{'nestkey':{'subnestkey':'final result'}}}
print(test)
print(test['key1'])
print(test['key1']['nestkey'])
print(test['key1']['nestkey']['subnestkey'])


