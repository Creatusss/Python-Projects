tasks = []

while True:
    task = input("Enter a task:\n")
    if task.lower() == "done":
        break
    tasks.append(task)
    
print("To Do List:")
for i in tasks:
    print(i)