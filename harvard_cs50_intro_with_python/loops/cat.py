# print("meow")
# print("meow")
# print("meow")
# print("meow")

# n= int(input("How many times should I meow? "))
while True:
   n = int(input("How many times should I meow? "))
   if n > 0:
      break


# while n > 0:
#    print("-.-meow", end="")
#    n -= 1

# for i in [0, 1, 2, 3]:       a list of numbers = [0, 1, 2, 3]
#    print("-.-meow", end="")
for _ in range(n):
   print("-.- meow", end=" ")
print()

print("@.@ meow\n"*n, end="")
