"""
#save arguments in a list
names = []

for _ in range(3):
   names.append(input("What's your name? "))

for name in sorted(names):
   print("Hello", name)
"""

#save data in a file with 'open'
# name = input("What's your name? ")

# file = open("names.txt", "a")
# file.write(name + "\n")
# file.close()

# name = input("What's your name? ")
# with open("names.txt", "a") as file:
#    file.write(name + "\n")

# with  open("names.txt", "r") as file:
#    lines = sorted( file.readlines())
# for line in lines:
#       print("Hello", line.strip())

names = []
with open("names.txt", "r") as file:
   for line in file:
      names.append(line.strip().capitalize())
      
for name in sorted(names):
   print("Hello", name)