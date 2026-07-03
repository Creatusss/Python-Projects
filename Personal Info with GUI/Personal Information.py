import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Personal Information")

mainLayout = QVBoxLayout()

row1 = QHBoxLayout()
nameinp = QLineEdit()
row1.addWidget(QLabel("Name"))
row1.addWidget(nameinp)

row2 = QHBoxLayout()
ageinp = QLineEdit()
row2.addWidget(QLabel("Age"))
row2.addWidget(ageinp)

row3 = QHBoxLayout()
nationinp = QLineEdit()
row3.addWidget(QLabel("Nationality"))
row3.addWidget(nationinp)

button1 = QPushButton("Submit")

mainLayout.addLayout(row1)
mainLayout.addLayout(row2)
mainLayout.addLayout(row3)
mainLayout.addWidget(button1)   

window.setLayout(mainLayout)

def printinfo():
    print(nameinp.text())
    print(ageinp.text())
    print(nationinp.text())

button1.clicked.connect(printinfo)

window.show()
app.exec()