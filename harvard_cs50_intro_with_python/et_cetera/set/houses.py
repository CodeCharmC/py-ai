students = [
   {"name": "Hermione", "house": "Gryffindor"},
   {"name": "Harry", "house": "Gryffindor"},
   {"name": "Ron", "house": "Gryffindor"},
   {"name": "Neville", "house": "Gryffindor"},
   {"name": "Draco", "house": "Slytherin"},
   {"name": "Hagrid", "house": "Gryffindor"},
   {"name": "Minerva", "house": "Gryffindor"},
   {"name": "Severus", "house": "Slytherin"},
   {"name": "Luna", "house": "Ravenclaw"},
   {"name": "Lupin", "house": "Slytherin"},
]

# get unique houses from this list of dictionaries by using a list
houses = []

for student in students:
   if student["house"] not in houses:
      houses.append(student["house"])

for house in sorted(houses):
   print(house)

print("-----")
# get unique houses from this list of dictionaries by using a set() 
houses = set()

for student in students:
   houses.add(student["house"])

for house in sorted(houses):
   print(house)