class Car:
  @staticmethod
  def start():
    print("car starting...")

  @staticmethod
  def stop():
    print("car stopping...")

class ToyotoCar(Car):
  def __init__(self, name):
    super().__init__()
    self.name = name

car1 = ToyotoCar("fortuner")

car1.start()
