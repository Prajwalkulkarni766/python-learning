# print elements of list in a single line

def print_lst_elements(lst):
  line_string = " "

  for ele in lst:
    line_string += str(ele)

  return line_string

print(print_lst_elements([10, 20, 30]))
print(print_lst_elements([10, 20, 30, 7, 8, 2, -1]))