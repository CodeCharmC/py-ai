# import random
# class Hat:
#    def __init__(self):
#       self.house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#    def sort(self, name):
#       print(name + " is in", random.choice(self.house))

# hat = Hat()
# hat.sort("Harry")

#or a better way by using classmethod
import random
class Hat:
   house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
   @classmethod
   def sort(cls, name):
      print(name + " is in", random.choice(cls.house))

Hat.sort("Harry")