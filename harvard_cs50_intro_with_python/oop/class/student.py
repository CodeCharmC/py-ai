class Student:
   def __init__(self, name, house):
      if not name:
         raise ValueError("Missing name")
      if not house:
         raise ValueError("Missing house")
      self.name = name
      self.house = house

def main():
   student = get_student()   
   print(f"{student.name} from {student.house}")

def get_student():
   name = input("Name: ").capitalize()
   house = input("House: ").capitalize()
   student = Student(name, house)   
   return student 

if __name__ == "__main__":
   main()