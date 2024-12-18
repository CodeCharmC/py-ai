# x = int(input("What's x? "))
# print(f"x is {x}")
# output could be
#ValueError: invalid literal for int() with base 10: 'y'  

#solution
# try:
#    x = int(input("What's x? "))
#    print(f"x is {x}")
# except ValueError:
#    print("x is not a number")


# try:
#    x = int(input("What's x? "))   
# except ValueError:
#    print("x is not a number")

# print(f"x is {x}")  
#will give an error of
#NameError: name 'x' is not defined   or scope error

#solution   
# try:
#    x = int(input("What's x? "))   
# except ValueError:
#    print("x is not a number")
# else:
#    print(f"x is {x}")

# a better solution
# while True:
#    try:
#       x = int(input("What's x? "))  
#       #break    its ok to break here
#    except ValueError:
#       print("x is not a number")
#    else:
#       break

#using function and tying out exceptions
def main():   
   x = get_int()
   print(f"x is {x}")

def get_int():
   while True:
      try:
         # x = int(input("What's x? "))
         # return x
         return int(input("What's x? "))         
      except ValueError:
         # print("x is not a number")
         pass
      # else:
      #    return x 
      
main()