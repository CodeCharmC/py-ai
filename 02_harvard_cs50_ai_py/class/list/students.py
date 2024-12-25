#An example of list in a class

class Students:
   def __init__(self, name):
      self.name = name
      self.courses = []

   def add_course(self, course):
      return self.courses.append(course)
   
#create instances
student = Students("Alixa")
student.add_course("History")
student.add_course("Math")
student.add_course("Physics")
print(student.courses)