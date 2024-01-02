# methods is function inside the body of the class.

class Circle:
    pi=3.14 # class variable  

    # auromatically envoked function for object and it is envoke when an object is created from the class
    def __init__(self,radius=5):
        self.radius=radius
        self.area=Circle.pi*radius*radius


c1=Circle()
print('The area is ',c1.area)


