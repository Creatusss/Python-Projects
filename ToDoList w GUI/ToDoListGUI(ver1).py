import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("To Do Application")


mainLayout =  QVBoxLayout()

row1 = QVBoxLayout()
uTask = QLineEdit()
buttonA = QPushButton("Submit")
row1.addWidget(QLabel("Enter a Task"))
row1.addWidget(uTask)
row1.addWidget(buttonA)

row2 = QVBoxLayout()
dTask = QLineEdit()
buttonD = QPushButton("Submit")
row2.addWidget(QLabel("Enter the number of task you wanted to Delete"))
row2.addWidget(dTask)
row2.addWidget(buttonD)

sTask = QPushButton("Click to see all the task")

tasks = []

def add():
    tasks.append(uTask.text())
    uTask.clear()
    print("Task added!")

def delete():
    rTask = int(dTask.text())
    tasks.pop(rTask - 1)
    dTask.clear()
    print("Task Deleted!")
    

def show():
    for task in tasks:
        print(task)

buttonA.clicked.connect(add)
buttonD.clicked.connect(delete)
sTask.clicked.connect(show)

mainLayout.addLayout(row1)
mainLayout.addLayout(row2)
mainLayout.addWidget(sTask)

window.setLayout(mainLayout)

window.show()
app.exec()