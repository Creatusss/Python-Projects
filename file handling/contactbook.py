print("==== Contact Book ====")
print("1.Add Contact\n2.View Contacts\n3.Exit")
    
    
while True:
    choice = float(input("Choose what you wanted to do: "))
   
    if choice == 1:
        name = input("Enter your Name:")
        pnumber = input("Enter your Phone Number:")
        with open("file handling/CB.txt", "a") as f:
            f.write(name + "\n")
            f.write(pnumber + "\n")

    if choice == 2:
        with open("file handling/CB.txt", "r") as g:
            print(g.read())

    if choice == 3:
        break

print("Thank you for using my program. Have a nice day!")

