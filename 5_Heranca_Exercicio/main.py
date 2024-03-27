class TaxPayer:
    def __init__(self, name, anual_income):
        self.Name = name
        self.Anual_income = anual_income

class Individual(TaxPayer):
    def __init__(self, name, anual_income, health_expenditures):
        super().__init__(name, anual_income)
        self.Health_expenditures = health_expenditures

    def Calculate_tax(self):
        if self.Anual_income < 20000:
            return self.Anual_income * 0.15 - self.Health_expenditures * 0.5
        else:
            return self.Anual_income * 0.25 - self.Health_expenditures * 0.5

class Company(TaxPayer):
    def __init__(self, name, anual_income, number_employee):
        super().__init__(name, anual_income)
        self.Number_employee = number_employee

    def Calculate_tax(self):
        if self.Number_employee > 10:
            return self.Anual_income * 0.14
        else:
            return self.Anual_income * 0.16


n = int(input("Enter the number of taxpayers: "))
taxpayers = []
total_collected_tax = 0

for i in range(n):
    print(f"\nTaxpayer data {i + 1}:")
    type = input("Individual or company (i/c)? ")
    name = input("Name: ")
    annual_income = float(input("Annual income: "))
    if type == 'i':
        health_expenses = float(input("Health expenses: "))
        taxpayer = Individual(name, annual_income, health_expenses)
    else:
        num_employees = int(input("Number of employees: "))
        taxpayer = Company(name, annual_income, num_employees)
    taxpayers.append(taxpayer)
    tax = taxpayer.Calculate_tax()
    print(f"Tax to be paid by {name}: $ {tax:.2f}")
    total_collected_tax += tax

print(f"\nTotal collected tax: $ {total_collected_tax:.2f}")