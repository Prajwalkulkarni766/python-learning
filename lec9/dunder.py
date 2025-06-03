# dunder functions are the function that starts with double underscore

class Complex:
  def __init__(self, real, img):
    self.real = real
    self.img = img

  def show_number(self):
    print(self.real, "i + ", self.img, "j", sep="")

  def __add__(self, another_obj):
    new_real = self.real + another_obj.real
    new_img = self.img + another_obj.img
    return Complex(new_real, new_img)


obj1 = Complex(1, 2)
obj2 = Complex(1, 2)
obj3 = obj1 + obj2
obj3.show_number()