#class Base:
    #attributes and methods

#class Child(Base):
    #Subclass attributes and methods

class Animal:
    def eat(self):
        print("Eating meat")
    def drink(self):
        print("Drinking water")
    def sleep(self):
        print("Sleeping")
class Bird(Animal):
    def fly(self):
        print("Flying")
    def chirp(self):
        print("Chirping")
    def feed(self):
        print("Feeding chicks")
lion=Bird()
lion.eat()
lion.drink()
lion.sleep()