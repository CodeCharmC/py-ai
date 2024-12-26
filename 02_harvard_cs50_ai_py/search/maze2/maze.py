

#class Node: the difference between class Node: and class Node(): is that class Node: is a class and class Node(): is a function that returns a class
class Node():
   def __init__(self, state, parent, action):
      self.state = state
      self.parent = parent
      self.action = action
   

class Frontier():
   def __init__(self):
      self.frontier = []

   def add_node(self, node):
      self.frontier.append(node)

   def contains_state(self, state):
      return any(node.state == state for node in self.frontier)
   
   def empty(self):
      return len(self.frontier) == 0
