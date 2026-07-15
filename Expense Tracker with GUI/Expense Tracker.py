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
totalPrice = 0
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


def addFeature():
    userExpense = expense.text()
    try:
        userAmount = int(amount.text())
        status.setText("Status: Ready")
        item = f"{userExpense} - ₱{userAmount}"

        global totalPrice
        totalPrice += userAmount

        expensesList.append(item)
        expensesListGUI.addItem(item)

        expense.clear()
        amount.clear()

        status.setText("Added")
        outputTotalExpenses.setText(f"Total Expenses: {totalPrice}")

    except ValueError:
        status.setText("Invalid Input")

    

def delFeature():
    deleteRow = expensesListGUI.currentRow()
    if deleteRow >= 0:
        expensesList.pop(deleteRow)
        expensesListGUI.takeItem(deleteRow)
        status.setText("Deleted")
    else:
        status.setText("Please Select a Task.")
    

addExpense.clicked.connect(addFeature)
amount.returnPressed.connect(addFeature)
deleteSelected.clicked.connect(delFeature)


mainLayout.addLayout(titleBar)
mainLayout.addLayout(userInputBar)
mainLayout.addLayout(actionBar)
mainLayout.addLayout(outputBar)

window.setLayout(mainLayout)


window.show()
app.exec()
