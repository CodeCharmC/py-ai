

#class Node: the difference between class Node: and class Node(): is that class Node: is a class and class Node(): is a function that returns a class
class Node():
   def __init__(self, state, parent, action):
      self.state = state
      self.parent = parent
      self.action = action
   