# find greatest number among 3

n1 = float(input("Enter first number : "))
n2 = float(input("Enter second number : "))
n3 = float(input("Enter third number : "))

if n1 > n2 and n1 > n3:
  print("Number 1 is greater than number 2 and 3")
elif n2 > n1 and n2 > n3:
  print("Number 2 is greater than number 1 and 3")
elif n3 > n2 and n3 > n1:
  print("Number 3 is greater than number 1 and 2")
else:
  print("Nither 1, 2 and 3.")