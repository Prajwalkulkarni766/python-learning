# define employee class with attribute role, department and salary have showDetails() method to display info

# create engineer class that inherits properties from employee and have attribute name and age

class Employee:
  def __init__(self, role, department, salary):
    self.role = role
    self.department = department
    self.salary = salary

  def showDetails(self):
    return f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}"
  

class Engineer(Employee):
  def __init__(self, role, department, salary, name, age):
    super().__init__(role, department, salary)
    self.name = name
    self.age = age


e1 = Engineer("Software engineer", "IT", 50000.00, "Ram", 25)
print(e1.showDetails())