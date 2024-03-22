class Employees:
    raise_amt = 2.0
    def __init__(self,name,gender,salary):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.email = name + "@gmail.com"
    def full_name(self):
        return self.name
    def salary_increase(self):
        self.salary =int(self.salary * self.raise_amt)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
class Developer(Employees):
    def __init__(self,name,gender,salary,program_lang):
        super().__init__(name,gender,salary) #shows that the contents in are borrowed from the parent
        self.program_lang = program_lang
class Receptionist(Employees):
    def __init__(self,name,gender,salary,age):
        super().__init__(name,gender,salary)
        self.age = age
Rec1=Receptionist("Harry","Male",60000,20)
Rec2=Receptionist("Mike","Male",89000,27)
print(f"{Rec1.name} is a {Rec1.gender},{Rec1.age}, earns {Rec1.salary}")
print(f"{Rec2.name} is a {Rec2.gender},{Rec2.age}, earns {Rec2.salary}")
developer1 = Developer("Cynthia","Female",79000,"Javascript")
developer2 = Developer("Chep","Female",60000,"Python")
print(f"{developer1.name} earns {developer1.salary} from {developer1.program_lang}")
print(f"{developer2.name} earns {developer1.salary} from {developer2.program_lang}")
emp1 = Employees("Grace", "Female", 200000)
emp2 = Employees("Mercy", "Female", 167000)
emp3 = Employees("Brian", "Male", 900000)
print(emp1.name)
print(emp2.name)
print(emp1.email)
print(emp2.email)
print(f"{emp1.name} is {emp1.gender} and earns {emp1.salary}")
print(f"{emp2.name} is {emp2.gender} and earns {emp2.salary}")
print(emp1.full_name())
print(emp1.salary)
emp1.salary_increase()
print(emp1.salary)
print(emp2.salary)
emp2.salary_increase()
print(emp2.salary)
Employees.raise_amt = 3
print(emp1.salary)
print(Employees.raise_amt)
print(emp3.salary)
emp3.salary_increase()
print(emp3.salary)

Employees.set_raise_amt(1.05)
print(Employees.raise_amt)
print(emp1.salary)
print(emp2.salary)

class Student:
    def __init__(self,first_name,last_name,maths,kisw):
        self.first_name = first_name
        self.last_name = last_name
        self.maths = maths
        self.kisw = kisw
    def total_marks(self):
        return self.maths + self.kisw
student1 = Student("John","Makau",70,58)
student2 = Student("Esther","Smith",80,90)
print(student1.total_marks())
print(student2.total_marks())
print(f"{student1.first_name} {student1.last_name} has greatly achieved marks {student1.total_marks()}")
print(f"{student2.first_name} {student2.last_name} has maintained her marks {student2.total_marks()}")

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
class Occupation(Person):
    def __init__(self,first_name,last_name,age,work):
        super().__init__(first_name, last_name,age)
        self.work = work
class Salary(Person):
    def __init__(self,first_name,last_name,age,salary):
        super().__init__(first_name,last_name,age)
        self.salary = salary
class Residence(Person):
    def __init__(self,first_name,last_name,age,town):
        super().__init__(first_name,last_name,age)
        self.town = town
occupation1 = Occupation("Janet","Smith",30,"Secretary")
occupation2 = Occupation("Ephy","Williams",30,"CEO")
print(f"{occupation1.first_name} {occupation1.last_name} aged {occupation1.age} is {occupation1.work}")
print(f"{occupation2.first_name} {occupation2.last_name} aged {occupation2.age} is {occupation2.work}")
salary1 = Salary("Mercy","Nyakio",20,90000)
salary2 = Salary("Kelvin","Porter",40,78900)
print(f"{salary1.first_name} {salary1.last_name} aged {salary1.age}, earns {salary1.salary}")
print(f"{salary2.first_name} {salary2.last_name} aged {salary2.age}, earns {salary2.salary}")
