#public attributes/methods
class Klasa:
    def __init__(self):
        self.public_variable = "public_variable"
my_class = Klasa()
print(f"Public variable: {my_class.public_variable}")

#protected attributes/methods
class Klasa_protected:
    def __init__(self):
        self._protected_variable = "protected_variable"
    def _protected_method(self):
        print("Protected method")

my_protected_class = Klasa_protected()
print(f"Protected variable: {my_protected_class._protected_variable}, Protected method: {my_protected_class._protected_method()}")