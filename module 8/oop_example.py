class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def calculate_area(self):
        return self.length*self.width
    def calculate_perimeter(self):
        return 2*(self.length+self.width)

my_rectangle = Rectangle(2, 5)
area=my_rectangle.calculate_area()
perimeter=my_rectangle.calculate_perimeter()

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

class Student:
    def __init__(self, name, percentage):
        self.name=name
        self.percentage=percentage

    def show(self):
        print("Name is", self.name, "and grade percentage is:", self.percentage)

stud=Student("Jessa", 80)
stud.show()

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old")

person1=Person("Alice",  15)
person2=Person("Bob", 17)

person1.greet()
person2.greet()

class Studenti:
    school_name="Digital School"
    def __init__(self, name, age, course):
        self.name=name
        self.age=age
        self.course=course

student1 = Studenti("Alice", 15, "Python")
student2 = Studenti("Bob", 17, "Javascript")
print(student1.school_name)
print(student1.course)
print(student2.course)
