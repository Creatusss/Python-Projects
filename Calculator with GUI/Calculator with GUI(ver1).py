import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QVBoxLayout
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()

mainLayout = QVBoxLayout()

header = QVBoxLayout()
top = QLabel("--------------------")
top.setAlignment(Qt.AlignmentFlag.AlignCenter)
title = QLabel("Calculator")
title.setAlignment(Qt.AlignmentFlag.AlignCenter)
bottom = QLabel("--------------------")
bottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
display = QLineEdit()

header.addWidget(top)
header.addWidget(title)
header.addWidget(bottom)
header.addWidget(display)

buttons = QGridLayout()
button7 = buttons.addWidget(QPushButton("7"), 0, 0)
button8 = buttons.addWidget(QPushButton("8"), 0, 1)
button9 = buttons.addWidget(QPushButton("9"), 0, 2)
buttonD = buttons.addWidget(QPushButton("/"), 0, 3)
button4 = buttons.addWidget(QPushButton("4"), 1, 0)
button5 = buttons.addWidget(QPushButton("5"), 1, 1)
button6 = buttons.addWidget(QPushButton("6"), 1, 2)
buttonM = buttons.addWidget(QPushButton("*"), 1, 3)
button1 = buttons.addWidget(QPushButton("1"), 2, 0)
button2 = buttons.addWidget(QPushButton("2"), 2, 1)
button3 = buttons.addWidget(QPushButton("3"), 2, 2)
buttonS = buttons.addWidget(QPushButton("-"), 2, 3)
buttonC = buttons.addWidget(QPushButton("C"), 3, 0)
button0 = buttons.addWidget(QPushButton("0"), 3, 1)
ButtonE = buttons.addWidget(QPushButton("="), 3, 2)
buttonA = buttons.addWidget(QPushButton("+"), 3, 3)

def pressButton():
    





mainLayout.addLayout(header)
mainLayout.addLayout(buttons)

window.setLayout(mainLayout)

window.show()
app.exec()
