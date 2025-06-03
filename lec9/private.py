# declaring private and protected attribute

class Account:
  def __init__(self, acc_no, acc_pass, balance):
    self.acc_no = acc_no
    # self.acc_pass = acc_pass - bad practice because password is the thing we dont want to make it public

    self.__acc_pass = acc_pass # good practice because it is accessible to only this class
    self.balance = balance

  def reset_pass(self, current_pass, new_pass):
    if self.__acc_pass != current_pass:
      print("Invalid password")
      return
    else:
      self.__acc_pass = new_pass

  def credit_amt(self, acc_pass, amt):
    if self.__acc_pass != acc_pass:
      print("Password mismatch ! Try again later")
      return
    else:
      self.balance += amt

  def debit_amt(self, acc_pass, amt):
    if self.__acc_pass != acc_pass:
      print("Password mismatch ! Try again later")
      return
    else:
      self.balance -= amt
  
