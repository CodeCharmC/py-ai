#a list
students_list = ["Harry", "Hermione", "Ron", "Draco", "Neville"]
houses_list = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin", "Gryffindor"]

# a dictionary
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

# for student in students_dict:
#    print(f"{student} is in {students_dict[student]}")


# a list with individual dictionaries
students_list_dict = [
   {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
   {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
   {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
   {"name": "Draco", "house": "Slytherin", "patronus": None},
   {"name": "Neville", "house": "Gryffindor", "patronus": None}
]

for student in students_list_dict:
   print(f"{student['name']} is in {student['house']} and their patronus is {student['patronus']}")