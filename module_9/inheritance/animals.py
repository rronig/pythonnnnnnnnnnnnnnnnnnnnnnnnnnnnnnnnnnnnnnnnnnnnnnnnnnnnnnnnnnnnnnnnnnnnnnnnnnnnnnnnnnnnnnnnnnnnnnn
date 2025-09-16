class Animal:
    def sound(self):
        print("Generic animal sounds are heard")
class Dog(Animal):
    def sound(self):
        print("Barking is heard")
class Cat(Animal):
    def sound(self):
        print("Meowing is heard")

animal=Animal()
animal.sound()
dog=Dog()
dog.sound()
cat=Cat()
cat.sound()