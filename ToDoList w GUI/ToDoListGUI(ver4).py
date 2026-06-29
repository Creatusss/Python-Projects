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

counter = QLabel("Task: 0")

def add():
    text = uTask.text().strip()

    if text == "":
        print("Task cannot be empty!")
        return
    
    tasks.append(text)
    taskList.addItem(text)

    uTask.clear()

    print("Task added!")
    counter.setText(f"Tasks: {len(tasks)}")

def delete():
    selected = taskList.currentRow()

    if selected >= 0:
        tasks.pop(selected)
        taskList.takeItem(selected)
    
    counter.setText(f"Tasks: {len(tasks)}")
 
buttonA.clicked.connect(add)
uTask.returnPressed.connect(add)
buttonD.clicked.connect(delete)

mainLayout.addWidget(counter)
mainLayout.addWidget(taskList)
mainLayout.addLayout(row1)
mainLayout.addLayout(row2)

window.setLayout(mainLayout)

window.show()
app.exec()