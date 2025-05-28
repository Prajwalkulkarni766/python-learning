word = "learning"

with open("practice.txt", "r") as f:
  data_line = f.readlines()
  line_number = 1
  for line in data_line:
    if word in line:
      print(f"word found in the file in line number {line_number}")
      break
    line_number += 1
  else:
    print("word not found in the file")

