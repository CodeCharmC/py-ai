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

# using list comprehension
gryffindors = [
   student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
   print(gryffindor)

#using filter function
# def is_gryffindor(student):
#    return student["house"] == "Gryffindor"

# gryffindors = filter(is_gryffindor, students)
# or
gryffindors = filter(lambda student: student["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda student: student["name"]):
   print(gryffindor["name"])