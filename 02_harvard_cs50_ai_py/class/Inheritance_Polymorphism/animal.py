#Inheritance and Polymorphism

#Inheritance allows one class (child class) to inherit attributes and methods from another class (parent class).

# Parent class
class Animal:
   def __init__(self, name):
      self.name = name

   def speak(self):
      print(f"This animal's name is {self.name}")
   
# Child class inheriting from Animal
class Dog(Animal):
   def __init__(self, name, breed):
      super().__init__(name) # Calls the constructor of the parent class
      self.breed = breed

   def speak(self):
      print(f"{self.name} barks!")
   

class Cat(Animal):
   def speak(self):
      print(f"{self.name} meaws!")
   

animal = Animal("Animal")
dog = Dog("Buddy", "Golden Retriever")
print(dog.breed)
cat = Cat("Whiskers")

animal.speak() 
# Here the same `speak()` method is used for both Dog and Cat, but it behaves differently this is "Polymorphism".The method speak() is overwritten in both Dog and Cat, so depending on the object (dog or cat), the method behaves differently. 
dog.speak() 
cat.speak()







