class Staff:
    def __init__(self,name,id,age):
        self.name = name
        self.id = id
        self.age = age
staff1 = Staff("Kenneth",123,35)
staff2 = Staff("Sally",453,30)
print(f"{staff1.name} who is ID {staff1.id} is {staff1.age} years old.")
print(f"{staff2.name} who is ID {staff2.id} is {staff2.age} years old.")
class Teacher(Staff):
    def __init__(self,name,id,age,work,school):
        super().__init__(name,id,age)
        self.work = work
        self.school = school
teacher1 = Teacher("Makenas",483,35,"HOD Mathematics","Makini")
teacher2 = Teacher("Japheth",256,30,"Secretary","Makini")
print(f"{teacher1.name} who is ID {teacher1.id} is {teacher1.age} years old with work {teacher1.work} at {teacher1.school} school.")
print(f"{teacher2.name} who is ID {teacher2.id} is {teacher2.age} years old with work {teacher2.work} at {teacher2.school} school.")
