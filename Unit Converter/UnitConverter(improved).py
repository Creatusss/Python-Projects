print("Welcome to Unit Converter")
print("1.kg to lbs\n2.lbs to kg\n3.°C to °F\n4.°F to °C")

print("Press 1 to convert kilogram (kg) to pounds (lbs)")
print("Press 2 to convert pounds (lbs) to kilogram (kg)")
print("Press 3 to convert Celsius (°C) to Fahrenheit (°F)")
print("Press 4 to convert Fahrenheit (°F) to Celsius (°C)\n")

def kgTlbs(kg):
    return kg * 2.20462

def lbsTkg(lbs):
    return lbs / 2.20462

def cTf(C):
    return (C*(9/5)) + 32

def fTC(F):
    return (F - 32) * (5/9)

while True:
    try:
        choice = int(input("Enter a number of conversion that you wanted to perform: "))

        if choice == 1:
            kg = float(input("Enter the value of a kg: "))
            print("The value of kg in lbs is ", kgTlbs(kg), " pounds.")

        elif choice == 2:
            lbs = float(input("Enter the value of a lbs: "))
            print("The value of lbs in kg is ", lbsTkg(lbs), " kilogram.")

        elif choice == 3:
            C = float(input("Enter the value of a Celsius: "))
            print("The value of Celcius in Fahrenheit is ", cTf(C), " °F")

        elif choice == 4:
            F = float(input("Enter the value of a Fahrenheit: "))
            print('The value of Fahrenheit in Celsius is ', fTC(F), " °C")

        else:
            print("Choose between 4 valid number")

    except ValueError:
        print("Enter a valid number!")
    
    again = input("Do you want to convert another value again?(yes/no): ")
    if again.lower() == "no":
        break

print("Thank you for using my Conversion Program!")