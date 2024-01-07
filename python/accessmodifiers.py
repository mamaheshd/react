# access modifie
#public
#private: double underscore(__) eg: self.__x access inside class only
#prtected: underscore(_) eg: self._x

class AccessTest:
    def __init__(self,a,b,c):
        self.a=a
        self.__b=b
        self._c=c

    def display(self):
        print(self.a)
        print(self.__b)
        print(self._c)

x=AccessTest(5,7,9)
print(x.a)
# print(x.b)
print(x._c)
x.display()