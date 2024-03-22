class Person:
    def __init__(self, first_name, last_name,age,height,weight):
        self.first_name = first_name
        self.last_name= last_name
        self.age= age
        self.height= height
        self.weight= weight
person1=Person("Valary","Smith",23,90,78)
person2=Person("Keith",'Johnson',45,89,90)
print(f"{person1.first_name} {person1.last_name} aged {person1.age} is of {person1.height} inches and weighs {person1.weight} kg")
print(f"{person2.first_name} {person2.last_name} aged {person2.age} is of {person2.height} inches and weighs {person2.weight} kg")
class Student(Person):
    def __init__(self,first_name,last_name,age,height,weight,grade):
        super().__init__(first_name,last_name,age,height,weight)
        self.grade= grade
s1 = Student("Marian","Flora",23,90,60,12)
s2 = Student("Jaime","Njuguna",20,78,90,11)
print(f"{s1.first_name} {s1.last_name} who is age {s1.age} is in grade {s1.grade} and is {s1.weight} kg of height {s1.height}.")
print(f"{s2.first_name} {s2.last_name} who is age {s2.age} is in grade {s2.grade} and is {s2.weight} kg of height {s2.height}.")
class Employee(Person):
    def __init__(self,first_name,last_name,age,height,weight,working_hours,salary):
        super().__init__(first_name,last_name,age,height,weight)
        self.working_hours = working_hours
        self.salary = salary
emp1 = Employee("Ruth","Nyakio",40,78,78,6,90000)
emp2 = Employee("Justin","Nyakundi",45,78,90,4,89400)
print(f"{emp1.first_name} {emp1.last_name} aged {emp1.age} works for {emp1.working_hours} hours and earns {emp1.salary}.")
print(f"{emp2.first_name} {emp2.last_name} aged {emp2.age} works for {emp2.working_hours} hours and earns {emp2.salary}.")