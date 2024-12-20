#difference between tupel_(), dictionary_{}, list_[] and class_[{},{},...]

class Student:
   ...

def main():
   student = get_student()   
   # print(f"{student[0]} from {student[1]}")#tuple  and list for both
   # print(f"{student['name']} from {student['house']}")#dictionary
   print(f"{student.name} from {student.house}")#class

def get_student():
   # name = input("Name: ").capitalize()
   # house = input("House: ").capitalize()
   student = Student()
   student.name = input("Name: ").capitalize()
   student.house = input("House: ").capitalize()

   # return (name, house) #tuple: a tuple is immutable
   # return [name, house] #list: a list is mutable/changeable
   # return {"name": name, "house": house} #dictionary: a dictionary is mutable   
   return student #class: a class is mutable


if __name__ == "__main__":
   main()