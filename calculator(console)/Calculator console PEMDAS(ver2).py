print("----------------------------------------")
print("Console Calculator".center(40))
print("----------------------------------------")

def calculate(expression):
        parts = expression.split()

        if len(parts) % 2 == 0:
            print("Invalid Expression")
            return
        
        while "*" in parts or "/" in parts:
            for i  in range(1, len(parts), 2):
                operator = parts[i]
                try:
                    leftNumber = float(parts[i - 1])
                    rightNumber = float(parts[i + 1])

                    if operator == "*" or operator == "/":
                            if operator == "*":
                                answer = leftNumber*rightNumber
                                parts[i-1:i+2] = [str(answer)]
                                break
                            else:
                                try:
                                    answer = leftNumber/rightNumber
                                    parts[i-1:i+2] = [str(answer)]
                                    break
                                except ZeroDivisionError:
                                    print("Math Error! Enter another expression without dividing 0")
                                    return
                except ValueError:
                    print("Invalid Expression!")
                    return
                            
                    
        while "+" in parts or "-" in parts:
            for i in range(1, len(parts), 2):
                try:  
                    operator = parts[i]
                    leftNumber = float(parts[i - 1])
                    rightNumber = float(parts[i + 1])

                    if operator == "+" or operator == "-":
                            if operator == "+":
                                answer = leftNumber+rightNumber
                                parts[i-1:i+2] = [str(answer)]
                                break
                            else:
                                answer = leftNumber-rightNumber
                                parts[i-1:i+2] = [str(answer)]
                                break
                except ValueError:
                     print("Invalid Expression!")
                     return
        print(parts[0])    
                 
while True:
    expression = input("Enter an expression: (type 'exit' to stop): ") 
    if expression == "exit":
        break
    calculate(expression)
