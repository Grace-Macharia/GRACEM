Height = float(input("Enter your height:"))
Weight = float(input("Enter your weight:"))
BMI = Weight/(Height*2)
print("Your BMI",BMI)
if BMI >1 and BMI <18:
    print("Underweight")
elif BMI >=18 and BMI <=24:
    print("Normal weight")
elif BMI >=25 and BMI <=30:
    print("Overweight")
elif BMI >=30:
    print("Abnormal")
else:
    print("Invalid")


