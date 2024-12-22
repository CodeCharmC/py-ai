students = ["Harry", "Hermione", "Ron", "Neville", "Draco", "Luna", "Lupin"]

# genaral way
for i in sorted(len(students)):
   print(i+1, students[i])

# enumerate way
for i, student in enumerate(sorted(students)):
   print(i+1, student)
