#Class Methods and Static Methods
#Class Method: Works with the class itself, not the instance. It takes cls as the first argument.
#Static Method: Does not require the class or instance to be passed. It works like a regular function inside the class.

class Person:
   _count = 0  # Class attribute

   def __init__(self,name):
      self.name = name
      Person._count += 1
   
   @classmethod      
   def count(cls):
      return cls._count  
   
   @staticmethod
   def greet():
      print("Hello")
   
# Create some instances
p1 = Person("Alixa")
p2 = Person("John")
p3 = Person("Sally")
p4 = Person("Tom")
print(Person.count())

Person.greet()