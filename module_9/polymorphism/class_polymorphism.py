class Dog:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"{self.name} barks")

class Cat:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"{self.name} meows")

class Bird:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print(f"{self.name} chirps")
dog = Dog("Qen")
cat = Cat("Jim")
bird=Bird("Bob")
for animal in (dog, cat, bird):
    animal.sound()