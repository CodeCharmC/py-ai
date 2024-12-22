
#example of unpacking for arguments
def f(*args, **kwargs):
   """
   *args is a tuple
   **kwargs is a dictionary

   """
   print("Positional arguments:", args)
   print("Named arguments:", kwargs)


f(100, 50, 25)
f(galleons=100, sickles=50, knuts=25)


#for print funtion
def print(*objects, sep=' ', end='\n', file=None):
   for o in objects:
      ...