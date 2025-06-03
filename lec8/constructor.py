class Student():

  # this will be common for all objects we are created and for this only one memory will be allocated
  college_name = "vp"

  # default constructor - if we not explicitly mention this then python will create auotmatically for us
  def __init__(self):
    print("adding new student")

  # parameterized constructor
  def __init__(self, name, roll_no, std):
    self.name = name
    self.roll_no = roll_no
    self.std = std

    print("Creating new student", self)

  # obj.attribute have higher precedance than class.attribute

s1 = Student("Ram", 10, 9)