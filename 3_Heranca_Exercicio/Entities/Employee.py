class Employee():
    def __init__(self, name, hire_date, position, salary):
        self.Name = name
        self.Hire_date = hire_date
        self.Position = position
        self.Salary = salary

    def Get_Name(self):
        self.Name

    def Set_Name(self, valor):
        self.Name = valor

    def Get_Hire_date(self):
        self.Hire_date

    def Set_Hire_date(self, valor):
        self.Hire_date = valor

    def Get_Salary(self):
        self.Salary

    def Set_Salary(self, valor):
        self.Salary = valor

    def __str__(self):
        return f"Employee's information: \n" \
        + f"Name: {self.Name}. Position: {self.Position}. Salary: ${str(self.Salary)}"