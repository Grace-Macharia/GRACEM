def hello_world():
    print("Hello World")
    print("Hello World")
    print("Hello World")
hello_world()
hello_world()
def nyumba(name):
    print(name)
    print(name)
    print(name)
nyumba("Grace")
nyumba("Bob")
def num(nambari):
    print(nambari)
    print(nambari)
    print(nambari)
num(56)
def num1(fname):
    print(fname + " is my favorite person")
num1("Wambo")
num1('Mom')
def students(first_name,last_name):
    print(first_name + last_name + " please enter your room")
students("Grace"," Macharia")
def employees(first_name,age):
    if age<20:
        print(first_name + "you are below 20 years old")
    elif age<=30:
        print(first_name + "you are middle aged")
    else:
        print(first_name + "you are older than 30 years old")
employees('Grace ',25)
employees('Jude ',34)
def age_calculator(age):
    new_age = age +10
    return new_age
calculated_age = age_calculator(20)
print(calculated_age)
def age_calculator(age):
    new_age = age - 7
    return new_age
calculated_age = age_calculator(19)
print(calculated_age)
print(age_calculator(20))
print(age_calculator(17))
print(age_calculator(22))
def peformance_calculator(*subjects):
    total = sum(subjects)
    return total
perf = peformance_calculator(45,56)
print(perf)
student2 = peformance_calculator(23,67)
print(student2)
student3 = peformance_calculator(23,56,67)
print(student3)
def country(nchi = "Ivory Coast"):
    return nchi
print(country("Jamaica"))
print(country("Britain"))
print(country("Kenya"))
def ongeza(x):
    return x * x
ongeza = ongeza(5)
print(ongeza)