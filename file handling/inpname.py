name = input("Enter your Name: ")

with open("file handling/nm.txt", "a") as f:
    f.write(f"\n{name}")

with open("file handling/nm.txt", "r") as g:
    print(g.read())