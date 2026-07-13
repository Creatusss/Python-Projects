import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QListWidget
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()

mainLayout = QVBoxLayout()

titleBar = QVBoxLayout()
top = QLabel("----------")
top.setAlignment(Qt.AlignmentFlag.AlignCenter)
title = QLabel("Expense Tracker")
title.setAlignment(Qt.AlignmentFlag.AlignCenter)
bottom = QLabel("----------")
bottom.setAlignment(Qt.AlignmentFlag.AlignCenter)

titleBar.addWidget(top)
titleBar.addWidget(title)
titleBar.addWidget(bottom)

userInputBar = QVBoxLayout()
expenseLabel = QLabel("Expense Name: ")
expense = QLineEdit()
amountLabel = QLabel("Amount: ")
amount = QLineEdit()

userInputBar.addWidget(expenseLabel)
userInputBar.addWidget(expense)
userInputBar.addWidget(amountLabel)
userInputBar.addWidget(amount)

actionBar = QHBoxLayout()
addExpense = QPushButton("Add Expense")
deleteSelected = QPushButton("Delete Selected")

actionBar.addWidget(addExpense)
actionBar.addWidget(deleteSelected)

outputBar = QVBoxLayout()
expensesList = []
expensesListGUI = QListWidget()
outputTop = QLabel("----------")
outputExpenseLabel = QLabel("Expenses: ")
outputBot = QLabel("----------")
outputTotalExpenses = QLabel("Total Expenses: ")
status = QLabel("Status: Ready")

outputBar.addWidget(outputTop)
outputBar.addWidget(outputExpenseLabel)
outputBar.addWidget(expensesListGUI)
outputBar.addWidget(outputBot)
outputBar.addWidget(outputTotalExpenses)
outputBar.addWidget(status)

def add():
    userExpense = expense.text()
    userAmount = int(amount.text())

    item = f"{userExpense} - ₱{userAmount}"

    expensesList.append(userExpense)
    expensesList.append(userAmount)
    expensesListGUI.addItem(item)

addExpense.clicked.connect(add)


mainLayout.addLayout(titleBar)
mainLayout.addLayout(userInputBar)
mainLayout.addLayout(actionBar)
mainLayout.addLayout(outputBar)

window.setLayout(mainLayout)


window.show()
app.exec()