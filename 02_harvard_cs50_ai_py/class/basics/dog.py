# 🐍

class Dog:
   def __init__(self, name, age, breed, size, color, weight):
      self.name = name
      self.age = age
      self.breed = breed
      self.size = size
      self.color = color
      self.weight = weight

   def bark(self):
      return f"{self.name} says woof! @.@"
   
   def spin(self):
      return f"A {self.breed} is spinning bitting it's {self.color} tail!"


#Create Objects (Instances of the Class)
my_dog = Dog("Ruby", 3, "Labrador", "Small", "White", 10)
your_dog = Dog("Buddy", 5, "Golden Retriever", "Medium", "Golden", 15)
her_dog = Dog("Max", 2, "Poodle", "Small", "Brown", 8)
#genaral info about dogs
# print(my_dog.breed)
# print(my_dog.name)
# print(your_dog.color)
# print(her_dog.name)
#lets make dogs do something using methods
print(my_dog.bark())
print(your_dog.spin())