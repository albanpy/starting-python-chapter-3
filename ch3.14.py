#Body Mass Index
weight=float(input("Enter your weight in pound:"))
height=float(input("Enter your height inch:"))
BMI=weight*(703/height**2)
print(f'Body mass index (BMI)={BMI:,.2f}')
if BMI>=18.5 and BMI<=25:
    print("Optimal Weight")
elif BMI<18.5:
    print("Underweight")
elif BMI>25:
    print("Overweight")
    