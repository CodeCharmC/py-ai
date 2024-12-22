
def main():
   n = int(input("What's n? "))
   for i in sheep(n):
      print(i)

def sheep(n):
   # flock = []
   # for i in range(n):
   #    flock.append("🐑")
   # return flock

   # using yield for solving mamory issue when n is extremely large
   for i in range(n):
      yield "🐑"*i      #iterator

if __name__ == "__main__":
   main()