# check list contain plaindrome or not

li = [1, 2, 3, 2, 1]

li_copy = li.copy()
li_copy.reverse()

print(li)
print(li_copy)

if li == li_copy:
  print("plaindrome")