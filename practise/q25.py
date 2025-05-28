word = "xlearning"

with open("practice.txt", "r") as f:
  data = f.read()

  if word in data:
    print("word found in the file")
  else:
    print("word not found in the file")
