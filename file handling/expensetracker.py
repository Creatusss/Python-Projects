print("Expense Tracker")
print("1.Add Expense\n2.View Expense\n3.Total Expense\n4.Exit")



while True:
    choice = input('Enter the number of the action that you wanted to do: ')

    if choice == "1":
        cat = input("Category: ")
        amnt = input("Amount: ")
        desc = input("Desc:")
        with open("file handling/ET.txt", "a") as f:
            f.write("Category: " + cat + "\n")
            f.write("Amount: " + amnt + "\n")
            f.write("Description: " + desc + "\n")

    elif choice == "2":
        with open("file handling/ET.txt", 'r') as g:
            print(g.read())

    elif choice == "3":
        total = 0
        with open("file handling/ET.txt", "r") as h:
            for line in h:
                if "Amount: " in line:
                    amt = line.split("Amount: ")[1]
                    total += int(amt)
        print(f"Total Expense is {total}")
    
    elif choice == "4":
        break

    else:
        print("Enter the Valid Number!")