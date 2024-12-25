#Magic Methods (Dunder Methods) 
#example
# __init__(self): Constructor (called when an object is created).
# __str__(self): Called by str() to print the object.
# __repr__(self): Called by repr() (used by the interpreter).
# __add__(self, other): Called when using the + operator.

class Point():
   def __init__(self, x, y):
      self.x = x 
      self.y = y

   def __add__(self, other):
      return Point(self.x + other.x, self.y + other.y) #When p1 + p2 is uesd, Python automatically calls p1.__add__(p2)
   
   def __sub__(self, other):
      return Point(self.x - other.x, self.y - other.y)
   
   def __str__(self):
      return f"Now the point is ({self.x}, {self.y})" #Without __str__, Python would display something like <__main__.Point object at 0x...>

#create instances
p1 = Point(1, 2)  
p2 = Point(3, 4)  
print(p1 + p2) #self = p1, other = p2
print(p2-p1) #self = p2, other = p1