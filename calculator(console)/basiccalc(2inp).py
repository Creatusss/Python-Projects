a = 0
b = 0

while True:
    try:
        a = float(input("Enter a first number: "))
        b = float(input("Enter a second number: "))
        op = input("Enter the operation that you wanted to use: (+,-,*,/)\n")
    
        if op == "+":
            print(f"Sum is {a+b}")
        
        elif op == "-":
            print(f"Difference is {a-b}")
        
        elif op == "*":
            print(f"Product is {a*b}")
            
        elif op == "/":
            print(f"Quotient is {a/b}")
            
        else:
            print("Invalid operator!")
            
    except ValueError:
        print("Enter a valid number or operation!")
       
    choice = input("Do you want to calculate again?\n" )
    if choice.lower() == "no":
        break
    
print("Thank you for using my basic calculator!")

    
    