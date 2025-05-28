# print all list element

def print_lst(lst, index=0):
    if index < len(lst):
        print(lst[index])
        print_lst(lst, index + 1)

print_lst([10, 20, 30])