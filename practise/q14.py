# while loop questions

# ------------------------------------------------------------------
# print from 1 to 100
# idx = 1
# while idx <= 100:
#   print(idx)
#   idx += 1

# ------------------------------------------------------------------
# print from 100 to 1
# idx = 100
# while idx >= 1:
#   print(idx)
#   idx -= 1

# ------------------------------------------------------------------
# print multiplication table
# n = int(input("Enter number to print its multiplication table : "))

# index = 1

# while index <= 10:
#   print(f"{n} x {index} = {n * index}")
#   index += 1

# ------------------------------------------------------------------
# print these elements using loop
# lst = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# index = 0

# while index < len(lst):
#   print(lst[index])
#   index += 1

# ------------------------------------------------------------------
# search number x in this tuple
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter element to search : "))

index = 0

while index < len(tup):
  if(x == tup[index]):
    print("Entered element found in the tuple")
    break
  index += 1
else:
  print("Entered element not found in the tuple")