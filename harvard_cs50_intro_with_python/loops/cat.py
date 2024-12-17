def main():
   num = get_num()
   meow(num)


def get_num():
   while True:
      n = int(input("How many times should I meow? "))
      if n > 0:
         return n

def meow(n):
   for _ in range(n):
      print("-.- meow", end=" ")

main()
