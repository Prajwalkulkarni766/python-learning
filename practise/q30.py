# define a circle class with radius r in constructor, it have area, perimeter

class Circle:
  def __init__(self, radius):
    self.radius = radius

  def area_of_circle(self):
    return 3.14 * pow(self.radius, 2)
  
  def perimeter_of_circle(self):
    return 2 * 3.14 * self.radius
  

c1 = Circle(5)
print(c1.area_of_circle())
print(c1.perimeter_of_circle())