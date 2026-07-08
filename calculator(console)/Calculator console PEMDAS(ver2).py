print("----------------------------------------")
print("Console Calculator".center(40))
print("----------------------------------------")

while True:
    expression = input("Enter an expression: (type 'exit' to stop): ") 
    if expression == "exit":
        break
    parts = expression.split()
    
    
    while "*" in parts or "/" in parts:
        for i  in range(1, len(parts), 2):
            operator = parts[i]
            leftNumber = float(parts[i - 1])
            if i + 1 >= len(parts):
                print("Invalid Expression!")
                break
            rightNumber = float(parts[i + 1])

            if operator == "*" or operator == "/":
                    if operator == "*":
                        answer = leftNumber*rightNumber
                        parts[i-1:i+2] = [str(answer)]
                    else:
                        try:
                            answer = leftNumber/rightNumber
                            parts[i-1:i+2] = [str(answer)]
                        except ZeroDivisionError:
                            print("Math Error! Enter another expression without dividing 0")
        
            break
                        
                

    while "+" in parts or "-" in parts:
        for i in range(1, len(parts), 2):   
            operator = parts[i]
            leftNumber = float(parts[i - 1])
            if i + 1 >= len(parts):
                print("Invalid Expression!")
                break
            rightNumber = float(parts[i + 1])

            if operator == "+" or operator == "-":
                    if operator == "+":
                        answer = leftNumber+rightNumber
                        parts[i-1:i+2] = [str(answer)]
                    else:
                        answer = leftNumber-rightNumber
                        parts[i-1:i+2] = [str(answer)]
            break
                    
        

    print(parts[0])
                       
