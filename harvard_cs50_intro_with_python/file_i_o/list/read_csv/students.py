import csv

name = input("What is your name? ").strip().title()
home = input("Where do you live? ").strip().title()

with open("students.csv", "a") as file:
   writer = csv.DictWriter(file, fieldnames=["Name", "Home"])
   writer.writerow({"Name": name, "Home": home})