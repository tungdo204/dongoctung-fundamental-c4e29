h = int(input("Enter your height: "))
w = int(input("Enter your weight: "))

h_m=h/100

BMI=w/(h_m**2)

if BMI<16:
    print("Severely underweight")
elif BMI <18.5:
    print("Underweight")
elif BMI <25:
    print("Normal")
elif BMI < 30:
    print("Overweight")
else:
    print("Obese")
    
