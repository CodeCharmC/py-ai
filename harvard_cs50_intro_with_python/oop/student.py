def main():
   student = get_student()   
   print(f"{student[0]} from {student[1]}")

def get_student():
   name = input("Name: ")
   house = input("House: ")
   return (name, house) #tuple a tuple is immutable
   # return [name, house] #list a list is mutable/changeable
   # return {"name": name, "house": house} #dictionary a dictionary is mutable


if __name__ == "__main__":
   main()