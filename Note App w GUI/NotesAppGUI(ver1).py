import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
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
save = QPushButton("Save")
load = QPushButton("Load")
clear = QPushButton("Clear")
actions.addWidget(save)
actions.addWidget(load)
actions.addWidget(clear)

status = QLabel("Ready")

def sv():
    with open ("notes.txt", "w") as f:
        text = note.toPlainText()
        f.write(text)
        status.setText("Note Saved!")

def ld():
    try:
        with open("notes.txt", "r") as g:
            content = g.read()
            note.setPlainText(content)
            status.setText("Note Loaded!")
    except:
        status.setText("File Does Not Exist")

def clr():
    note.clear()
    status.setText("Note Cleared!")

save.clicked.connect(sv)
load.clicked.connect(ld)
clear.clicked.connect(clr)

mainLayout.addLayout(header)
mainLayout.addWidget(status)
mainLayout.addLayout(body)
mainLayout.addLayout(actions)

window.setLayout(mainLayout)

window.show()
app.exec()
 