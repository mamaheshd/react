# methods is function inside the body of the class.

class Circle:
    pi=3.14 # class variable  

    # auromatically envoked function for object and it is envoke when an object is created from the class
    def __init__(self,radius=5):
        self.radius=radius
        self.area=Circle.pi*radius*radius
    # defining the own method
    def setRadius(self,newradius):
        self.radius=newradius
        self.area=self.pi*newradius*newradius
        

c1=Circle()
print('The area is ',c1.area)

# calling the method
c1.setRadius(10)
print('New radius is ',c1.radius)
print('The area is ',c1.area)