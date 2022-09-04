height = float(input("enter your height in m"))
weight = float(input("enter your weight in kg"))


BMI= weight / (height/100)**2

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <25.0:
    print("normal")
elif BMI >= 25 and BMI <30:
    print("overweight")
elif BMI >= 30:
    print("obese")