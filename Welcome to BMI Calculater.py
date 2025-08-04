print("Welcome to BMI Calculater.")
weight = float(input("Enter your weight: "))
height = float(input("Enter your Height: "))
bmi = weight / (height ** 2)
print(bmi)
if bmi <= 18.5:
    print("You are Underweight")

elif 18.5 < bmi <= 25:
    print("Normal Weight")

else:
    print("You are Overweight")