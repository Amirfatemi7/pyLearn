import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from functools import partial

def showWins(p):
    msg_box = QMessageBox(text = " tabrik player  (" + p + ")  wins")
    clean()
    msg_box.exec()

def clean():
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")
            buttons[i][j].setStyleSheet("background-color: black;")

def check():
    if buttons[0][0].text() == 'X' and buttons[1][1].text() == 'X' and buttons[2][2].text() == 'X':
        showWins('X')
    if buttons[0][2].text() == 'X' and buttons[1][1].text() == 'X' and buttons[0][0].text() == 'X':
        showWins('X')
    if buttons[0][0].text() == 'O' and buttons[1][1].text() == 'O' and buttons[2][2].text() == 'O':
        showWins('O')
    if buttons[0][2].text() == 'O' and buttons[1][1].text() == 'O' and buttons[0][0].text() == 'O':
        showWins('O')    
    for j in range(3):
        x = 0
        o = 0
        for i in range(3):
            if buttons[i][j].text() == 'X':
                x +=1
            if buttons[i][j].text() == 'O':
                o +=1
            if x >= 3:
                showWins('X')
            if o >= 3:
                showWins('O')
    for i in range(3):
        x = 0
        o = 0
        for j in range(3):
            if buttons[i][j].text() == 'X':
                x +=1
            if buttons[i][j].text() == 'O':
                o +=1
            if x >= 3:
                showWins('X')
            if o >= 3:
                showWins('O')
    # showWins(" O = X ")
   

def play(row, col):
    global player,buttons
    if player == 1:
        buttons[row][col].setText("X")
        buttons[row][col].setStyleSheet("color: red; background-color: pink;")
        player = 2
        check()
    else:
        buttons[row][col].setText("O")
        buttons[row][col].setStyleSheet("color: blue; background-color: lightblue;")
        player = 1
        check()



app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load("/mnt/e/hosh/pyLearn/assignment18/TicTacToe.ui")
main_window.show()

player = 1

buttons = [[main_window.pushButton_1, main_window.pushButton_2, main_window.pushButton_3],
           [main_window.pushButton_4, main_window.pushButton_5, main_window.pushButton_6],
           [main_window.pushButton_7, main_window.pushButton_8, main_window.pushButton_9]]

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(play, i, j))


app.exec()


