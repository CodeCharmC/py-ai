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

# get unique houses from this list of dictionaries
houses = []

for student in students:
   if student["house"] not in houses:
      houses.append(student["house"])

for house in sorted(houses):
   print(house)