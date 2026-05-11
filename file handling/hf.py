import os

with open("file handling/helloworld.txt", "w") as f:
    f.write("Hello dlrow\n")
    f.write("Hi world\n")

with open("file handling/helloworld.txt", "r") as g:
    print(g.read())

with open("file handling/helloworld.txt", "a") as h:
    h.write("www")
with open("file handling/helloworld.txt", "r") as g:
    print(g.read())

if os.path.exists("file handling/helloworld.txt"):
    print("File Exist!")
else:
    print("File Not Exist!")