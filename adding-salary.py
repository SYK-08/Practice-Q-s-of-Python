class Employee:
    append_employee = 0
    bonus = 5000

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.append_employee += 1 #This appends the the number of employees by the number of employees added.

    def increase(self):
        self.salary = self.salary + Employee.bonus
    
print(Employee.append_employee) #used here
shreyash = Employee("Shreyash", 50000)
ritu = Employee("Ritupallav", 50000)
print(Employee.append_employee)
mrin = Employee("Mrinmay", 50000)
print(Employee.append_employee)
# print(shreyash.salary)
# shreyash.increase()
# print(shreyash.salary)