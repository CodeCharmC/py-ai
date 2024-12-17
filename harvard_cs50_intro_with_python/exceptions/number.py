# x = int(input("What's x? "))
# print(f"x is {x}")
# output could be
#ValueError: invalid literal for int() with base 10: 'y'  

#solution
try:
   x = int(input("What's x? "))
   print(f"x is {x}")
except ValueError:
   print("x is not a number")