# inheritance is to fprm a new classes from the classes that have been already defined. The newly formed class are called derived class and the class that are derive from are called base class. The deive class overide or extends the functionalities of base class.

class Animal:
    def __init__(self):
        print('Animal class is created')

    def intro(self):
        print('animal')
    
    def eat(self):
        print('Animal who eat')

class Dog(Animal):
    def intro(self):
        print('The animal type is dog')

    def speak(self):
        print('dog barks')

obj_a=Animal()
obj_a.intro()
obj_a.eat()

obj_d=Dog()
obj_d.intro()
obj_d.eat()
obj_d.speak()
