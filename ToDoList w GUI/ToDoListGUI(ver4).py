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
buttonD = QPushButton("Delete Selected Text")
row2.addWidget(buttonD)

tasks = []
taskList = QListWidget()

counter = QLabel("Tasks: 0")
status = QLabel("")

def add():
    text = uTask.text().strip()

    if text == "":
        status.setText("Task cannot be empty!")
        uTask.clear()
        return
    
    if text in tasks:
        status.setText("Task already exist!")
        uTask.clear()
        return
    
    tasks.append(text)
    taskList.addItem(text)

    uTask.clear()

    status.setText("Task added!")
    counter.setText(f"Tasks: {len(tasks)}")

def delete():
    selected = taskList.currentRow()

    if selected >= 0:
        tasks.pop(selected)
        taskList.takeItem(selected)
        status.setText("Task Deleted!")
    else:
        status.setText("Please select a task.")
    
    counter.setText(f"Tasks: {len(tasks)}")
 
buttonA.clicked.connect(add)
uTask.returnPressed.connect(add)
buttonD.clicked.connect(delete)

mainLayout.addWidget(counter)
mainLayout.addWidget(status)
mainLayout.addWidget(taskList)
mainLayout.addLayout(row1)
mainLayout.addLayout(row2)

window.setLayout(mainLayout)

window.show()
app.exec()
