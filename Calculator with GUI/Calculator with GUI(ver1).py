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
message = QLabel("")
display = QLineEdit()
display.setReadOnly(True)

header.addWidget(top)
header.addWidget(title)
header.addWidget(bottom)
header.addWidget(message)
header.addWidget(display)

buttons = QGridLayout()
button7 = QPushButton("7")
button8 = QPushButton("8")
button9 = QPushButton("9")
buttonDivision = QPushButton("/")
button4 = QPushButton("4")
button5 = QPushButton("5")
button6 = QPushButton("6")
buttonMultiplication = QPushButton("*")
button1 = QPushButton("1")
button2 = QPushButton("2")
button3 = QPushButton("3")
buttonSubtraction = QPushButton("-")
buttonClear = QPushButton("C")
button0 = QPushButton("0")
buttonPoint = QPushButton(".")
buttonAddition = QPushButton("+")
buttonBackspace = QPushButton("⌫")
buttonEqual = QPushButton("=")

buttons.addWidget(button7, 0, 0)
buttons.addWidget(button8, 0, 1)
buttons.addWidget(button9, 0, 2)
buttons.addWidget(buttonDivision, 0, 3)
buttons.addWidget(button4, 1, 0)
buttons.addWidget(button5, 1, 1)
buttons.addWidget(button6, 1, 2)
buttons.addWidget(buttonMultiplication, 1, 3)
buttons.addWidget(button1, 2, 0)
buttons.addWidget(button2, 2, 1)
buttons.addWidget(button3, 2, 2)
buttons.addWidget(buttonSubtraction, 2, 3)
buttons.addWidget(buttonClear, 3, 0)
buttons.addWidget(button0, 3, 1)
buttons.addWidget(buttonPoint, 3, 2)
buttons.addWidget(buttonAddition, 3, 3)
buttons.addWidget(buttonBackspace, 4, 0)
buttons.addWidget(buttonEqual, 4, 1, 1, 3)

def pressButton(number):
    currentDisplay = display.text()
    display.setText(currentDisplay + number)

def clr():
    display.clear()
    message.clear()

def dl():
    currentDisplay = display.text()
    display.setText(currentDisplay[:-1])


def eq():
    expression = display.text()
    if expression == "":
        return
    try:
        result = eval(expression)
        display.setText(str(result))
        message.clear()
    except ZeroDivisionError:
        message.setText("Division by zero is not allowed(press C to clear)")
        display.clear()
    except Exception:
        message.setText("Invalid Expression!")
        display.clear()


button7.clicked.connect(lambda: pressButton("7"))
button8.clicked.connect(lambda: pressButton("8"))
button9.clicked.connect(lambda: pressButton("9"))
buttonDivision.clicked.connect(lambda: pressButton("/"))
button4.clicked.connect(lambda: pressButton("4"))
button5.clicked.connect(lambda: pressButton("5"))
button6.clicked.connect(lambda: pressButton("6"))
buttonMultiplication.clicked.connect(lambda: pressButton("*"))
button1.clicked.connect(lambda: pressButton("1"))
button2.clicked.connect(lambda: pressButton("2"))
button3.clicked.connect(lambda: pressButton("3"))
buttonSubtraction.clicked.connect(lambda: pressButton("-"))
button0.clicked.connect(lambda: pressButton("0"))
buttonPoint.clicked.connect(lambda: pressButton("."))
buttonAddition.clicked.connect(lambda: pressButton("+"))

buttonClear.clicked.connect(clr)
buttonBackspace.clicked.connect(dl)
buttonEqual.clicked.connect(eq)


mainLayout.addLayout(header)
mainLayout.addLayout(buttons)

window.setLayout(mainLayout)

window.show()
app.exec()
