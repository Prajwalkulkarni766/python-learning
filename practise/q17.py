# write a function to print length of list

def calculate_len_of_lst(lst):
  lenght = 0

  for i in lst:
    lenght += 1

  return lenght

print("length of list : ", calculate_len_of_lst([10, 20, 30]))
print("length of list : ", calculate_len_of_lst([10, 20, 30, 7, 8, 2, -1]))