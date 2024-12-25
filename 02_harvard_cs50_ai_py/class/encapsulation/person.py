#Encapsulation is the concept of hiding the internal details of an object and only exposing the necessary parts 
#Python "mangles" the names of attributes that start with __ (double underscores) to _ClassName__attributeName

class Person:
   def __init__(self, name, age, gender):
      self._name = name
      self.__age = age
      self.gender = gender
   
   def get_age(self):
      # print(f"{self._name} is now {self.__age} years old")
      return self.__age
   
   def set_age(self, age):
      if age > 0 and age <= 120:
         self.__age  = age
      else:
         print("Invalid age")

person_1 = Person("Alixa", 18, "Female")

person_1.get_age()  
# person_1.set_age(-5)
# person_1.set_age(0)
# person_1.set_age(150)
person_1.set_age(120)
# print(f"{person_1._name} is now {person_1.__age} years old")
#OUTPUT:
# AttributeError: 'Person' object has no attribute '__age'. Did you mean: '_name'?

#SOLUTION:
print(f"{person_1._name} is now {person_1._Person__age} years old")
#or
print(f"{person_1._name} is now {person_1.get_age()} years old")