class Animal:
   def __init__(self, name):
      self.name = name

   def speak(self):
      print(f"{self.name} makes a sound.")

class Dog(Animal):
   def __init__(self, name, breed):
      super().__init__(name) 
      self.breed = breed

   def speak(self):
      print(f"{self.name} barks.")

dog = Dog("Buddy", "Golden Retriever")
dog1 = Animal("Bob", "German Shepherd")
dog2 = Dog("Rex", "Labrador")
dog3 = Dog("Max","Poodle")
dog4 = Dog("Rover", "Golden Retriever")
dog5 = Dog("Charlie", "Golden Retriever")

dog.speak() 
dog1.speak()