from abc import ABC,abstractmethod

class polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(polygon):
    def __init__(self,b,h):
        self.b=b
        self.h=h

    def area(self):
        return 0.5*self.b*self.h
    
x=Triangle(5,10)
print(x.area())