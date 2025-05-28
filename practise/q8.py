# find multiple of 7 or not

num = int(input("Enter a number to find it is multiple of 7 or not : "))

result = num % 7

if result == 0:
  print("Entered number is multiple of 7")
else:
  print("Entered number is not a multiple of 7")

print(result)