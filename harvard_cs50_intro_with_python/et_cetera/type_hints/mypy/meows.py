# pep install mypy

def meow(n: int) -> str:
   # for _ in range(n):
   #    print("meow")
   return "meow" * n

# number: int = input("Number of meows: ")  --> error found by mypy to be unsolved
number: int = int(input("Number of meows: "))
meows: str = meow(number)
print(meows)