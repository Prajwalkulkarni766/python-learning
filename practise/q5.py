# odd or even

num = int(input("Enter a number to check whether it is odd or even : "))

status = num % 2

if status == 0:
  print("Entered number is even")
else:
  print("Entered number is odd")