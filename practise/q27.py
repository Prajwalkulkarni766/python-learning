with open("practice2.txt", "r") as f:
  data = f.readlines()

  for line in data:
    # print(line)

    line_data = line.split(", ")
    print(line_data)  

    for data in line_data:
      if int(data)%2 == 0:
        print(data, " is even number")