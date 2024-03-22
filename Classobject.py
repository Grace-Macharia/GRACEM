class Student:
    name = 'Grace'
    age = 16
print(Student.name)
print(Student.age)
print(f'Name: {Student.name} Age: {Student.age}') #f helps to print the objects inserted
class Employees:
    name = 'Kyra'
    marital_status = 'Married'
    monthly_salary = 45000
print(Employees.name)
print(Employees.marital_status)
print(Employees.monthly_salary)
print(f'Name: {Employees.name} '
      f'Married: {Employees.marital_status} '
      f'Salary: {Employees.monthly_salary}')
class Parents:
    first_name = 'John'
    last_name = 'Maina'
parents1 = Parents()
print(parents1.first_name)
print(parents1.last_name)
print(f'Name: {parents1.first_name} {parents1.last_name}')
class Parent:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
parents1 = Parent('Samuel','Job')
parents2 = Parent('Esther','Kinuthia')
print(parents1.first_name)
print(f'first name:{parents1.first_name} last name:{parents1.last_name}')
print(parents2.first_name)
print(f'first is: {parents2.first_name} last name:{parents2.last_name}')

class Presidents:
    def __init__(self,country,first_name):
        self.country = country
        self.first_name = first_name
president1 = Presidents('Kenya','Jomo')
print(f'country: {president1.country} first_name: {president1.first_name}')
president2 = Presidents('Tanzania','Sameer')
print(f'country: {president2.country} first_name: {president2.first_name}')
class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
        print(f'{self.first_name} {self.last_name} is {self.age}' " years old")
    def display(self):
        print(f'{self.age}')
Person1 = Person('Samuel','Njuguna',32)
print(Person1.full_name())
print(Person1.display())
Person2 = Person('Joy','Samuel',28)
print(Person2.full_name())
print(Person2.display())