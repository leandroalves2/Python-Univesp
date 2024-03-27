from Entities.Employee import Employee

class Manager(Employee):
    def __init__(self, name, hire_date, position, salary):
        super().__init__(name, hire_date, position, salary)
    def Brut_salary(self):
        attSalary = self.Salary + (self.Salary * 0.25)
        return attSalary

    def __str__(self):
        return f"Employee's information: \n" \
            + f"Name: {self.Name}. Position: {self.Position}. Salary: ${str(self.Brut_salary())}"