class Student:
  def __init__(self, name):
    self.name = name

s1 = Student("ram")
print(s1)
del s1
print(s1)