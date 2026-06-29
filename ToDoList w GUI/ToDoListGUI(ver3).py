import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget

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
buttonD = QPushButton("Delete")
row2.addWidget(QLabel("Enter the number of task you wanted to Delete"))
row2.addWidget(dTask)
row2.addWidget(buttonD)

tasks = []
taskList = QListWidget()

def add():
    text = uTask.text().strip()

    if text == "":
        print("Task cannot be empty!")
        return
    
    tasks.append(text)
    taskList.addItem(text)

    uTask.clear()

    print("Task added!")

def delete():
    selected = taskList.currentRow()

    if selected >= 0:
        tasks.pop(selected)
        taskList.takeItem(selected)
 
buttonA.clicked.connect(add)
uTask.returnPressed.connect(add)

buttonD.clicked.connect(delete)
dTask.returnPressed.connect(delete)

mainLayout.addWidget(taskList)
mainLayout.addLayout(row1)
mainLayout.addLayout(row2)

window.setLayout(mainLayout)

window.show()
app.exec()
