import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtUiTools import QUiLoader


class mainwindow(QWidget):
    def __init__(self):
        super(mainwindow, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()

        self.game = [[None for i in range(3)]for j in range(3)]
        self.game[0][0] = self.ui.btn0_0
        self.game[0][1] = self.ui.btn0_1
        self.game[0][2] = self.ui.btn0_2
        self.game[1][0] = self.ui.btn1_0
        self.game[1][1] = self.ui.btn1_1
        self.game[1][2] = self.ui.btn1_2
        self.game[2][0] = self.ui.btn2_0
        self.game[2][1] = self.ui.btn2_1
        self.game[2][2] = self.ui.btn2_2

        self.ui.show()
        self.player = 1
        self.player1_wins = 0
        self.player2_wins = 0
        self.cpu = [0, 1, 2]

        for i in range(3):
            for j in range(3):
                self.game[i][j].clicked.connect(partial(self.play, i, j))

    def play(self, i, j):

        if self.game[i][j].text() == '':
            if self.player == 1:
                self.game[i][j].setText('X')
                self.game[i][j].setStyleSheet(
                    'color: blue;background-color:#CCFFFF')
                self.player = 2
# --------------------cpu---------------------------------------------
                if self.ui.rb_pc.isChecked():
                    while True:
                        row = random.randint(0, 2)
                        col = random.randint(0, 2)
                        if self.game[row][col].text() == '':
                            self.game[row][col].setText('O')
                            self.game[row][col].setStyleSheet(
                                'color: red;background-color:#FFCCCC')
                            self.player = 1
                            break
# ------------------------------------------------------------------------
            elif self.player == 2:
                if self.ui.rb_pp.isChecked():
                    self.game[i][j].setText('O')
                    self.game[i][j].setStyleSheet(
                        'color: red;background-color:#FFCCCC')
                    self.player = 1
        self.check()

    def check(self):
        # -----------------------PLAYER1--------------------------
        if all(self.game[0][i].text() == 'X' for i in range(3)):
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 1 برنده شد")
            msg.exec_()
        elif all(self.game[1][i].text() == 'X' for i in range(3)):
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 1 برنده شد")
            msg.exec_()
        elif all(self.game[2][i].text() == 'X' for i in range(3)):
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 1 برنده شد")
            msg.exec_()
        elif all(self.game[i][0].text() == 'X' for i in range(3)):
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 1 برنده شد")
            msg.exec_()
        elif all(self.game[i][1].text() == 'X' for i in range(3)):
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 1 برنده شد")
            msg.exec_()
        elif all(self.game[i][2].text() == 'X' for i in range(3)):
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 1 برنده شد")
            msg.exec_()
        elif self.game[0][0].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][2].text() == 'X':
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 1 برنده شد")
            msg.exec_()
        elif self.game[0][2].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][0].text() == 'X':
            self.player1_wins += 1
            self.ui.lbl_player1.setText(str(self.player1_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 1 برنده شد")
            msg.exec_()

# -------------------------PLAYER2-----------------------------------------
        if all(self.game[0][i].text() == 'O' for i in range(3)):
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 2 برنده شد")
            msg.exec_()
        elif all(self.game[1][i].text() == 'O' for i in range(3)):
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 2 برنده شد")
            msg.exec_()
        elif all(self.game[2][i].text() == 'O' for i in range(3)):
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 2 برنده شد")
            msg.exec_()
        elif all(self.game[i][0].text() == 'O' for i in range(3)):
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 2 برنده شد")
            msg.exec_()
        elif all(self.game[i][1].text() == 'O' for i in range(3)):
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 2 برنده شد")
            msg.exec_()
        elif all(self.game[i][2].text() == 'O' for i in range(3)):
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 2 برنده شد")
            msg.exec_()
        elif self.game[0][0].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][2].text() == 'O':
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 2 برنده شد")
            msg.exec_()
        elif self.game[0][2].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][0].text() == 'O':
            self.player2_wins += 1
            self.ui.lbl_player2.setText(str(self.player2_wins))
            msg = QMessageBox()
            msg.setText("بازیکن شماره 2 برنده شد")
            msg.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = mainwindow()
    sys.exit(app.exec_())
