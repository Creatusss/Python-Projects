import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Student Grade Manager")

mainLayout = QVBoxLayout()

titleBar = QVBoxLayout()
top = QLabel("----------")
top.setAlignment(Qt.AlignmentFlag.AlignCenter)
title = QLabel("Studen Grade Manager")
title.setAlignment(Qt.AlignmentFlag.AlignCenter)
bottom = QLabel("----------")
bottom.setAlignment(Qt.AlignmentFlag.AlignCenter)

titleBar.addWidget(top)
titleBar.addWidget(title)
titleBar.addWidget(bottom)

userInputBar = QVBoxLayout()
studentNameGuide = QLabel("Student Name:")
studentName = QLineEdit()
quiz1Guide = QLabel("Quiz 1:")
quiz1 = QLineEdit()
quiz2Guide = QLabel("Quiz 2:")
quiz2 = QLineEdit()
quiz3Guide = QLabel("Quiz 3:")
quiz3 = QLineEdit()

userInputBar.addWidget(studentNameGuide)
userInputBar.addWidget(studentName)
userInputBar.addWidget(quiz1Guide)
userInputBar.addWidget(quiz1)
userInputBar.addWidget(quiz2Guide)
userInputBar.addWidget(quiz2)
userInputBar.addWidget(quiz3Guide)
userInputBar.addWidget(quiz3)

actionsBar = QHBoxLayout()
calculate = QPushButton("Calculate")
clear = QPushButton("Clear")

actionsBar.addWidget(calculate)
actionsBar.addWidget(clear)

displayBar = QVBoxLayout()
average = QLabel("Average: ")
status = QLabel("Status: ")
letterGrade = QLabel("Letter Grade: ")
errorMessage = QLabel("")

displayBar.addWidget(average)
displayBar.addWidget(status)
displayBar.addWidget(letterGrade)
displayBar.addWidget(errorMessage)

def avg():
    try:
        quiz1Input = float(quiz1.text())
        quiz2Input = float(quiz2.text())
        quiz3Input = float(quiz3.text())

        if studentName.text().strip() == "":
            raise ValueError
        if not (0 <= quiz1Input <= 100 and 0 <= quiz2Input <= 100 and 0 <= quiz3Input <= 100):
            raise ValueError

        errorMessage.setText("")

        ave = (quiz1Input+quiz2Input+quiz3Input)/3
        average.setText(f"Average: {ave}")

        if 90 <= ave <= 100:
            status.setText("Status: Passed")
            letterGrade.setText("Letter Grade: A")

        elif 80 <= ave <= 89.9:
            status.setText("Status: Passed")
            letterGrade.setText("Letter Grade: B")

        elif 70 <= ave <= 79.9:
            if 75 <= ave <= 79.9:
                status.setText("Status: Passed")
                letterGrade.setText("Letter Grade: C")
            else:
                status.setText("Status: Fail")
                letterGrade.setText("Letter Grade: C")

        elif 60 <= ave <= 69.9:
            status.setText("Status: Fail")
            letterGrade.setText("Letter Grade: D")

        else:
            status.setText("Status: Fail")
            letterGrade.setText("Letter Grade: F")

    except ValueError:
        errorMessage.setText("Invalid Input!")

def clr():
    studentName.clear()
    quiz1.clear()
    quiz2.clear()
    quiz3.clear()

    average.setText("Average: ")
    status.setText("Status: ")
    letterGrade.setText("Letter Grade: ")
    errorMessage.setText("")


calculate.clicked.connect(avg)
clear.clicked.connect(clr)


mainLayout.addLayout(titleBar)
mainLayout.addLayout(userInputBar)
mainLayout.addLayout(actionsBar)
mainLayout.addLayout(displayBar)

window.setLayout(mainLayout)

window.show()
app.exec()
