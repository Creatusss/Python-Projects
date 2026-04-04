import math
print("Hello, Welcome to BMI Calculator")
print("\nBMI CATEGORIES")
print("1.Underweight:18.5 Below\n2.Normal:18.5-24.9\n3.Overweight:25-29.9\n4.Obese:30 and above")

kg = float(input("Enter your Weight(kg) here: "))
m = float(input("Enter your Height(m) here: "))
    
bmi = kg/math.pow(m, 2)
print(f"Your BMI is {bmi}")

if bmi < 18.5:
    print("You are classified as Underweight")

elif 18.5 <= bmi <= 24.9:
    print("You are classified as Normal")

elif 25 <= bmi <= 29.9:
    print("You are classified as Overweight")

else:
    print("You are classified as Obese")