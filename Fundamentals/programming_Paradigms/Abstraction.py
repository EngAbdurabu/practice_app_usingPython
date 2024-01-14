"""
# we use this modul for make class abstract 
from abc import ABC, abstractmethod
# this is abstract class inheritace from ABC modul
class Shape (ABC):
    # this is abstract funtion becuase use decorators before it 
    @abstractmethod
    def area(self):
        pass
    def info(self):
        return "this is a shape area"
        
class Square (Shape):
    def __init__(self, side):
        self.side = side
    def area (self):
        return self.side ** 2
class Triangle (Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return (self.base *self.height) / 2
class Circle (Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

square= Square (4)
print (square.area())
triangle = Triangle(6, 8)
print(triangle.area())
circle = Circle(5)
print(circle.area())
print(circle.info())
"""
