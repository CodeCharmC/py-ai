import re 
name = input("What's your name? ").strip().title()

if (matches := re.search(r"^(.+), *(.+)$", name)):
   name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")

# :=  also known as walrus operator. it will assign a value to a variable and ask a boolean question
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