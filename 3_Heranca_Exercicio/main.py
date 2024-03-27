from Entities.Employee import Employee
from Entities.Manager import Manager

print("Enter the employee's information:")
name = input("Name: ").title()
hire_date = input("Hire date (dd/mm/yyyy): ")
position = input("position in the company: ").title()
salary = float(input("Salary: "))

if position == "Manager":
    manager = Manager(name, hire_date, position, salary)
    print()
    print(manager)
else:
    employee = Employee(name, hire_date, position, salary)
    print()
    print(employee)


