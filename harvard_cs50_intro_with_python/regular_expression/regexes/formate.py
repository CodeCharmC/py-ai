import re 
name = input("What's your name? ").strip().title()

if " " in name:
   first, last = name.split(" ")
   print(f"{last} {first}")
else:
   print(name)

