from abc import ABC, abstractmethod
import math
#class ClassName(ABC):
#    pass
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*(self.radius**2)
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base*self.height)/2
circle = Circle(7)
square = Square(5)
triangle = Triangle(3,4)
print(circle.area())
print(square.area())
print(triangle.area())