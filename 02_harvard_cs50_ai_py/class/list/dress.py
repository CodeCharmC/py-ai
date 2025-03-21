
class Dress:
   def __init__(self, key, value):
      self.key = key
      self.value = value
      self.bio = {}
      
   def __str__(self):
      return f"{self.key}: {self.value}"

   def add_bio(self):
      self.bio.append(Dress.__str__(self))      
   
   def show_bio(self):
      return Dress.add_bio(self)
   
bio1 = {"name":"alixa"}
bio2 = {"age":"8"}
bio3 = {"gender":"female"}
bio4 = {"hobby":"coding"}
bio5 = {"expertise":"python"}

print(bio1, bio2, bio3, bio4, bio5)