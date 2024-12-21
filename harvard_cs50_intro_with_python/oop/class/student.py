class Student:
   def __init__(self, name, house, patronus=""):      
      self.name = name
      self.house = house
      # self.patronus = patronus

   def __str__(self):
      return f"{self.name} from {self.house}"
   
   @property            #Getter
   def name(self):
      return self._name
   
   @name.setter        #Setter
   def name(self, name):
      if not name:
         raise ValueError("Missing name")
      self._name = name
   
   @property            #Getter
   def house(self):
      return self._house

   @house.setter        #Setter
   def house(self, house): 
      if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
         raise ValueError("Invalid house")
      self._house = house
      

   # def charm(self):
   #    match self.patronus:
   #       case "Stag":
   #          return "🦌"
   #       case "Otter":
   #          return "🦦"
   #       case "Jack Russell terrier":
   #          return "🐕"
   #       case _:
   #          return "🪄" 

def main():
   student = get_student() 
   print(student)  
   # print("Expecto Patronum!")
   # print(student.charm())   
   # print(f"{student.name} from {student.house}")

def get_student():
   name = input("Name: ").capitalize()
   house = input("House: ").capitalize()
   patronus = input("Patronus: ").capitalize()
   return Student(name, house, patronus)   

if __name__ == "__main__":
   main() 