import sys

# print("Hello, my name is", sys.argv[1])

# output could be IndexError: list index out of range

#solution
try:
   print("Hello, my name is", sys.argv[1])
except IndexError:
   print("Missing name")

# another solution
if len(sys.argv) < 2:
   print("Too few names")
elif len(sys.argv) > 2:
   print("Too many names")
else:
   print("Hello, my name is", sys.argv[1])
