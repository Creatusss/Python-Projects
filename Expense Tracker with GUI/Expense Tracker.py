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
    userExpense = expense.text().strip()
    for existingExpense, existingAmount in expensesList:
        if userExpense.lower() == existingExpense.lower():
            status.setText("Warning: Duplicate Expense")
            expense.clear()
            amount.clear()
            return
    try:
        userAmount = int(amount.text())
        if not userExpense or userAmount <= 0:
            raise ValueError
        
        status.setText("Status: Ready")

        global totalPrice
        totalPrice += userAmount

        expensesList.append((userExpense, userAmount))#Tuple so that the individual records are immutable, also so that it can be as one object
        expensesListGUI.addItem(f"{userExpense} - ₱{userAmount}")

        expense.clear()
        amount.clear()

        status.setText("Status: Added")
        outputTotalExpenses.setText(f"Total Expenses: ₱{totalPrice}")

    except ValueError:
        status.setText("Warning: Invalid Input")


def delFeature():
    deleteRow = expensesListGUI.currentRow()
    if deleteRow >= 0:
        userExpense, userAmount = expensesList[deleteRow]

        global totalPrice
        totalPrice -= userAmount 

        expensesList.pop(deleteRow)
        expensesListGUI.takeItem(deleteRow)

        status.setText("Status: Deleted")
        outputTotalExpenses.setText(f"Total Expenses: ₱{totalPrice}")
    else:
        status.setText("Warning: Please Select a Task.")
    

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
