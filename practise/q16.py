# finding out sum 
# lst = [0, 1]
# index = 0
# sum = 0

# while index < len(lst):
#   sum += lst[index]
#   index += 1

# print("sum : ", sum)

# find factorial of n number

n = int(input("Enter number to find its factorial : "))
factorial = 1

for i in range(n, 0, -1):
  factorial *= i

print("factorial : ", factorial)