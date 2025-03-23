#Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):
   @abstractmethod
   def area(self):
      pass

class Tringle(Shape):
   def __init__(self, base, height):
      self.base = base
      self.height = height

   def area(self):
      return 0.5*self.base*self.height
   
blue_tringle = Tringle(10, 5)
print(blue_tringle.area())

class Rectangle(Shape):
   def __init__(self, length, width):
      self.length = length
      self.width = width

   def area(self):
      return self.length*self.width
   
red_rectangle = Rectangle(10, 5)
print(red_rectangle.area())

class Circle(Shape):
   def __init__(self, radius):
      self.radius = radius

   def area(self):
      return 3.14*self.radius*self.radius 
   
green_circle = Circle(10)
print(green_circle.area())