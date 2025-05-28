# a block of code to perform specific task
# a and b is parametere

def add(a, b):
  return a + b

# 5 and 7 is argument here
# print(add(5, 7))

# average of 3 number
def calculate_avg(n1, n2, n3):
  return (n1 + n2 + n3) / 3

# print(calculate_avg(10, 20, 30))

# default parameter
def mul(a = 1, b = 1):
  return a * b

print(mul(10))