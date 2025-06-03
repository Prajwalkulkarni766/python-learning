# suppose your one class attribute is dependent on another class attribute and you want to update that whenever a small changes happens

class Student:
  def __init__(self, phy, chem, maths):
    self.phy = phy
    self.chem = chem
    self.maths = maths

  @property
  def percentage(self):
    return str((self.phy + self.chem + self.maths) / 3) +"%"
  

s1 = Student(98, 97, 99)
print(s1.percentage)
s1.phy = 88
print(s1.percentage)