print("Welcome to Unit Converter")
print("1.kg to lbs\n2.lbs to kg\n3.°C to °F\n4.°F to °C")

print("Press 1 to convert kilogram (kg) to pounds (lbs)")
print("Press 2 to convert pounds (lbs) to kilogram (kg)")
print("Press 3 to convert Celsius (°C) to Fahrenheit (°F)")
print("Press 4 to convert Fahrenheit (°F) to Celsius (°C)\n")

choice = int(input("Enter your choice here: "))

if choice == 1:
    kg = float(input("Enter the value of the Kilogram: "))
    lbs = kg * 2.20462
    print(lbs)

elif choice == 2:
    lbs = float(input("Enter the value of the Pounds: "))
    kg = lbs/2.20462
    print(kg)    
    
elif choice == 3:
    C = float(input("Enter the value of the Celsius: "))
    F = (C * (9/5)) + 32
    print(F)
 
elif choice == 4:
    F = float(input("Enter the value of the Fahrenheit: "))
    C = (F - 32) * (5/9)
    print(C)
    
else:
    print("Enter a number between 1-4. Thank you and Have a great Day!")