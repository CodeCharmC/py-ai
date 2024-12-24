

class Student:
   def __init__(self, name, age, _class):
      self.name = name
      self.age = age
      self._class = _class
   
   def attendence(self):
      return f"{self.name} is attending the class {self._class}\'s homeroom class!"

class GraduateStudent(Student):
   def thesis_topic(self, topic):
      return f"{self.name}\'s thesis topic is {topic}"


student_1= Student("Alix", 18, 12)
student_2= Student("Sally", 14, 7)
student_3= GraduateStudent("John", 20, 12)
print(student_3.thesis_topic("Biology"))
print(student_1.name)
print(student_1._class)
print(student_1.attendence())
print(student_2.name)
print(student_2._class)
print(student_2.attendence())
