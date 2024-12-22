students = ["Hermione", "Harry", "Ron", "Neville", "Draco", "Hagrid", "Minerva", "Severus", "Luna", "Lupin"]

# using list comprehension
gryffindors = []
for student in students:
   gryffindors.append({"name": student, "house": "Gryffindor"})
print(gryffindors)

#or using list comprehension

gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)

#or using dictionary comprehension

gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)