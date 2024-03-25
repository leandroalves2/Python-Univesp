from Person import Person

print("First-person data:")
name = input("Name: ")
age = int(input("Age: "))
p1 = Person(name, age)

print("Secund-person data:")
name2 = input("Name: ")
age2 = int(input("Age: "))
p2 = Person(name2, age2)

if p1.Age > p2.Age:
    print(f"Pessoa mais velha: {p1.Name}")
else:
    print(f"Pessoa mais velha: {p2.Name}")
