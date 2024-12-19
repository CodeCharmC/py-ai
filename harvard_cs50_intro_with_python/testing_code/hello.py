
def main():
   print("What is your name?")
   name = input().strip().title()
   print(hello(name))

def hello(to="world"):
   return f"Hello, {to}!"   # using return because print returns None which will not work in pytest

if __name__ == "__main__":
   main()