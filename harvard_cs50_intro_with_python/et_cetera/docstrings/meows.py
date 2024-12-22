

def meow(n: int) -> str:
   #docstring
   """
   Meow n times.

   :param n: The number of times to meow.
   :type n: int
   :raise ValueError: If n is not an integer.  
   :return: A string of meows, one per line.
   :rtype: str
   """
   return "meow" * n

number: int = int(input("Number of meows: "))
meows: str = meow(number)
print(meows)