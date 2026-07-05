print("----------------------------------------")
print("Console Calculator".center(40))
print("----------------------------------------")

while True:
    expression = input("Enter an expression: (type 'exit' to stop): ") 
    if expression == "exit":
        break
    parts = expression.split()
    result = float(parts[0])

    for i in range(1, len(parts), 2):
        try:
            operator = parts[i]
            number = float(parts[i + 1])

            if operator == "+":
                result += number
                print(f"Result: {result}")

            elif operator == "-":
                result -= number
                print(f"Result: {result}")

            elif operator == "*":
                result *= number
                print(f"Result: {result}")

            elif operator == "/":
                result /= number
                print(f"Result: {result}")

        except (ValueError, IndexError):
            print("Invalid Expression")

        except ZeroDivisionError:
            print("Cannot Divide by Zero")

   
    

