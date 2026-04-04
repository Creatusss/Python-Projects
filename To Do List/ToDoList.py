print("Hello! Welcome to To Do List Program")
print("1.Add a Task\n2.Remove a Task\n3.View the Tasks\n4.Exit")

task = [] 
while True:
    choice = int(input("Enter a Number(1-4) to choose what you desire to do in To Do List Program: "))

    if choice == 1:
        while True:
            ATask = input("Enter your task here: ")
            if ATask == "stop":
                break
            task.append(ATask)

    elif choice == 2:
        print(task)
        while True:
            RTask = (input("Enter the number of the task that you wanted to remove here: "))
            if RTask == "stop":
                break
            else:
                task.pop(int(RTask) - 1)
        print(task)

    elif choice == 3:
        print(task)

    elif choice == 4:
        break

    else:
        print("Enter a Valid Number!")
        
print("Thank you for using my program!")