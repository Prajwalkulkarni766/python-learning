# take marks of 3 subject and store them into dictory

info = {}

for i in range(3):
  key = input("Enter name of subject : ")
  value = int(input("Enter marks received in this project : "))
  info[key] = value

print("Info : ", info)