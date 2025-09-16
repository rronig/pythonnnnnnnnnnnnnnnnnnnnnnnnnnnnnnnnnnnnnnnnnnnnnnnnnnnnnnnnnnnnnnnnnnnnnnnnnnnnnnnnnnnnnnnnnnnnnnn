class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("Some generic animal sounds are heard")
    def description(self):
        print(f"This is an animal named {self.name}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        print("Barking is heard")
    def description(self):
        super().description()
        print(f"Breed is {self.breed}")
class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed
    def sound(self):
        print("Meowing is heard")
    def description(self):
        super().description()
        print(f"Breed is {self.breed}")

animal=Animal("Generic Animal")
animal.sound()
animal.description()
cat=Cat("Snowball", "Russian blue")
cat.sound()
cat.description()
dog=Dog("Max", "Newfoundland")
dog.sound()
dog.description()