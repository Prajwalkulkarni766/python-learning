with open("practice.txt", "r+") as f:
  data = f.read()
  print("original content", data)
  data = data.replace("java", "python")
  f.write(data)
  print("updated content", data)