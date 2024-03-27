class Person():
    def __init__(self, name, age, gender):
        self.Name = name
        self.Age = age
        self.Gender = gender

class Student(Person):
    def __init__(self, name, age, gender, registration):
        super().__init__(name, age, gender)
        self.Registration = registration

    def study(self):
        print(f"{self.Name} is study")

class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.Subject = subject

    def teaching(self):
        print(f"{self.Name} is teaching {self.Subject}")

student1 = Student("Leandro", 28, 'M', 1234)
teacher1 = Teacher("Nelio", 30, 'M', "Algorithm")

student1.study()
teacher1.teaching()
