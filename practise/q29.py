class Account():
  def __init__(self, acc_no, balance):
    self.balance = balance
    self.acc_no = acc_no

  def credit(self, amt):
    self.balance += amt

  def debit(self, amt):
    self.balance -= amt

  def print_balance(self):
    print(f"Account no.: {self.acc_no} and balance: {self.balance}")

a1 = Account("123456", 100)
a1.print_balance()
a1.credit(100)
a1.print_balance()
a1.debit(10)
a1.print_balance()