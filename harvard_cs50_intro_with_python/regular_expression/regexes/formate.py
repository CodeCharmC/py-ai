import re 
name = input("What's your name? ").strip().title()

matches = re.search(r"^(.+), (.+)$", name)
if matches:
   last, first = matches.groups()
   name = f"{first} {last}"
print(f"Hello, {name}")


#. means any character
#^ means start
#$ means end
# + means one or more
# * means zero or more
# ? means zero or one
#.+ means one or more characters
# \d means digit
# \w means word
# \s means space
# \D means not digit
# \W means not word
# \S means not space
# (..) means group
# | means or
# \A means start of string
# \Z means end of string