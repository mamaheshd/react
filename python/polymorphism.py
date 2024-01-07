# polymorphism means many form of same methods and they behave differently in different classes.

class Bird:
    def intro(self):
        print('there are many types of birds')
    
    def fly(self):
        print("Many of the birds can fly but some of them can't fly")

class Parrot(Bird):
    def fly(self):
        print('Parrot can fly')

obj_b=Bird()
obj_b.intro()
obj_b.fly()

obj_p=Parrot()
obj_p.intro()
obj_p.fly()