
def main():
   print("What is your name?")
   name = input().strip().title()
   hello(name)

def hello(to="world!"):
   print("Hello,", to)

if __name__ == "__main__":
   main()