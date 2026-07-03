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
button7 = QPushButton("7")
button8 = QPushButton("8")
button9 = QPushButton("9")
buttonD = QPushButton("/")
button4 = QPushButton("4")
button5 = QPushButton("5")
button6 = QPushButton("6")
buttonM = QPushButton("*")
button1 = QPushButton("1")
button2 = QPushButton("2")
button3 = QPushButton("3")
buttonS = QPushButton("-")
buttonC = QPushButton("C")
button0 = QPushButton("0")
buttonE = QPushButton("=")
buttonA = QPushButton("+")

buttons.addWidget(button7, 0, 0)
buttons.addWidget(button8, 0, 1)
buttons.addWidget(button9, 0, 2)
buttons.addWidget(buttonD, 0, 3)
buttons.addWidget(button4, 1, 0)
buttons.addWidget(button5, 1, 1)
buttons.addWidget(button6, 1, 2)
buttons.addWidget(buttonM, 1, 3)
buttons.addWidget(button1, 2, 0)
buttons.addWidget(button2, 2, 1)
buttons.addWidget(button3, 2, 2)
buttons.addWidget(buttonS, 2, 3)
buttons.addWidget(buttonC, 3, 0)
buttons.addWidget(button0, 3, 1)
buttons.addWidget(buttonE, 3, 2)
buttons.addWidget(buttonA, 3, 3)

def pressButton(number):
    currentDisplay = display.text()
    display.setText(currentDisplay + number)

def clr():
    display.clear()



button7.clicked.connect(lambda: pressButton("7"))
button8.clicked.connect(lambda: pressButton("8"))
button9.clicked.connect(lambda: pressButton("9"))
buttonD.clicked.connect(lambda: pressButton("/"))
button4.clicked.connect(lambda: pressButton("4"))
button5.clicked.connect(lambda: pressButton("5"))
button6.clicked.connect(lambda: pressButton("6"))
buttonM.clicked.connect(lambda: pressButton("*"))
button1.clicked.connect(lambda: pressButton("1"))
button2.clicked.connect(lambda: pressButton("2"))
button3.clicked.connect(lambda: pressButton("3"))
buttonS.clicked.connect(lambda: pressButton("-"))
button0.clicked.connect(lambda: pressButton("0"))
buttonA.clicked.connect(lambda: pressButton("+"))

buttonC.clicked.connect(clr)

#buttonE



mainLayout.addLayout(header)
mainLayout.addLayout(buttons)

window.setLayout(mainLayout)

window.show()
app.exec()
