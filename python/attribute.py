# attributes property,characteristic of an object

#defining the class
#function inside class is methods
class Student:
    def __init__(self,full_name,age,address):
        #defining the attribute
        self.name=full_name
        self.age=age
        self.address=address
        self.batch='DUR01'


#instance of class or it is known as object
obj_mahesh=Student(full_name='Mahesh Dahal', age='25',address='ktm')
# to access the attributes of the class
print(obj_mahesh.name)
print(obj_mahesh.age)
print(obj_mahesh.address)
print(obj_mahesh.batch)

#another objects
obj_lushan=Student(full_name='Lushan', age='24',address='btm')
print(obj_lushan.name)
print(obj_lushan.age)
print(obj_lushan.address)
print(obj_lushan.batch)

