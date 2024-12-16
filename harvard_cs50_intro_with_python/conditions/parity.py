def main():
   x =  int(input("What's x?"))
   if is_even(x):
      print("Even")
   else:
      print("Ood")

def is_even(n):
   # return True if n % 2 == 0 else False    simplified version
   return n % 2 == 0          #the most simplified version
      
main()