# create a student class take marks of 3 subject and write a method which returns avg of taken marks

class Student():
  def __init__(self, name, physics_marks, chemistry_marks, maths_marks):
    self.name = name
    self.physics_marks = physics_marks
    self.chemistry_marks = chemistry_marks
    self.maths_marks = maths_marks

  def avg(self):
    return (self.physics_marks + self.chemistry_marks + self.maths_marks) / 3
  
s1 = Student("Ram", 96, 95, 98)
print(s1.avg())