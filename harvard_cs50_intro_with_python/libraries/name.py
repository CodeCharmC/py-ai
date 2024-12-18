import sys

# print("Hello, my name is", sys.argv[1])

# output could be IndexError: list index out of range

#solution
# try:
#    print("Hello, my name is", sys.argv[1])
# except IndexError:
#    print("Missing name")

# another solution
if len(sys.argv) < 2:
   sys.exit("Too few names")
elif len(sys.argv) > 2:
   sys.exit("Too many names")

print("Hello, my name is", sys.argv[1])