students_list = ["Harry", "Hermione", "Ron", "Draco", "Neville"]
houses_list = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin", "Gryffindor"]


students_dict = {
   "Harry": "Gryffindor", 
   "Hermione": "Gryffindor",
   "Ron": "Gryffindor",
   "Draco": "Slytherin", 
   "Neville": "Gryffindor"
}

# print(students_dict["Hermione"])
# print(students_dict.get("Harry"))
# print(students_dict.get("Neville"))

for student in students_dict:
   print(f"{student} is in {students_dict[student]}")