name = input("What is your name? ").strip().title()

# if name == "Harry" or name == "Hermione" or name == "Ron":
#    print("Gryffindor")
# elif name == "Draco":
#    print("Slytherin")
# else:
#    print("Who are you?")

# or

match name:
   case "Harry" | "Hermione" | "Ron":
      print("Gryffindor")
   case "Draco":
      print("Slytherin")
   case _:
      print("Who are you?")