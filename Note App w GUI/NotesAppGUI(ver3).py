import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox, QFileDialog
from PyQt6.QtCore import Qt

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("NotePad")

mainLayout = QVBoxLayout()

header = QVBoxLayout()
top = QLabel("--------------------------------------------------")
top.setAlignment(Qt.AlignmentFlag.AlignCenter)
title = QLabel("    Notepad    ")
title.setAlignment(Qt.AlignmentFlag.AlignCenter)
bottom = QLabel("--------------------------------------------------")
bottom.setAlignment(Qt.AlignmentFlag.AlignCenter)
header.addWidget(top)
header.addWidget(title)
header.addWidget(bottom)

body = QVBoxLayout()
note = QTextEdit()
body.addWidget(note)

actions = QHBoxLayout()
new = QPushButton("New")
save = QPushButton("Save")
load = QPushButton("Load")
clear = QPushButton("Clear")
actions.addWidget(new)
actions.addWidget(save)
actions.addWidget(load)
actions.addWidget(clear)

status = QLabel("Ready")
characterCounter = QLabel(f"Characters : ")
wordCounter = QLabel(f"Words: ")

def updateCounter():
    text = note.toPlainText()
    characterCountWithoutSpace = len(text.replace(" ", "").strip())
    wordCounterWithoutSpace = len(text.split())
    characterCounter.setText(f"Characters : {characterCountWithoutSpace}")
    wordCounter.setText(f"Words: {wordCounterWithoutSpace}")
    
def nw():
    note.clear()
    status.setText("Ready")
    updateCounter()


def sv():
    filename, _ = QFileDialog.getSaveFileName(window, "Save a File", "", "Text Files (*.txt);;Python Files (*.py);;CPP Files (*.cpp);;All Files (*)")
    if not filename:
        return
    with open (filename, "w") as f:
        text = note.toPlainText()
        f.write(text)
        status.setText("Note Saved!") 
        updateCounter()

def ld():
    filename, _ = QFileDialog.getOpenFileName(window, "Open a File", "", "Text Files (*.txt);;Python Files (*.py);;CPP Files (*.cpp);;All Files (*)")
    if not filename:
        return
    try:
        with open(filename, "r") as g:
            content = g.read()
            note.setPlainText(content)
            status.setText("Note Loaded!")
            updateCounter()
    except FileNotFoundError:
        status.setText("File Does Not Exist")
        updateCounter()

def clr():
    confirmation = QMessageBox.question(window, "Confirmation Required", "Are you sure?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    if confirmation == QMessageBox.StandardButton.Yes:
        note.clear()
        status.setText("Note Cleared!")
        updateCounter()
    elif confirmation == QMessageBox.StandardButton.No:
        return
    
new.clicked.connect(nw)
save.clicked.connect(sv)
load.clicked.connect(ld)
clear.clicked.connect(clr)

mainLayout.addLayout(header)
mainLayout.addWidget(status)
mainLayout.addLayout(body)
mainLayout.addWidget(characterCounter)
mainLayout.addWidget(wordCounter)
mainLayout.addLayout(actions)

window.setLayout(mainLayout)

window.show()
app.exec()
 