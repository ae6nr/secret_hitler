#
#
#
# pyuic5 mainwindow.ui -o Ui_MainWin.py
#

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QInputDialog

import PyQt5
from Ui_MainWin import Ui_MainWindow
from Ui_PlayerWin import Ui_Form
from SecretHitler import SecretHitler



class MainWindow:
    def __init__(self):
        
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.sender_email = "" # enter the email that will be used to send emails
        self.sender_email_password = "" # enter your password
        self.emaildict = {
            "Bryan" : "player1@gmail.com",
            "Kristen" : "player2@gmail.com",
            "Jason" : "player3@gmail.com",
            "Bryant" : "player4@gmail.com",
            "Jackson" : "player5@gmail.com",
            "Monica" : "player6@gmail.com",
            "Josh" : "player7@gmail.com",
            "Aleska" : "player8@gmail.com",
            "Benj" : "player9@gmail.com",
            "Judith" : "player0@gmail.com"
        }

        self.startNewGame()
        self.updatePresInfo()

        # Connect signals to slots
        self.ui.pushButton_pass.clicked.connect(self.pass_sequence)
        self.ui.pushButton_reveal.clicked.connect(self.reveal_party)
        self.ui.pushButton_examine.clicked.connect(self.examine)
        self.ui.pushButton_enact.clicked.connect(self.enact)
        self.ui.actionStart_New_Game.triggered.connect(self.startNewGame)
        #self.ui.actionUpdate_Players.triggered.connect(self.updatePlayers)
        self.ui.comboBox_president.currentIndexChanged.connect(self.updatePresInfo)

    def show(self):
        self.main_win.show()

    def updatePresInfo(self):
        msg = self.ui.comboBox_president.currentText() + " is the president."
        self.ui.statusbar.showMessage(msg)
        self.ui.label_pres_info_1.setText(msg)
        self.ui.label_pres_info_2.setText(msg)

    def startNewGame(self, sendemails=False):
        self.sh = SecretHitler(self.emaildict, self.sender_email, self.sender_email_password, sendemails=sendemails) # To actually send emails, set sendemails=True
        msg = "Welcome to a new round of Secret Hitler!"
        self.ui.label_3.setText(msg)

    def getOption(self, title="Decision"):
        i, okPressed = QInputDialog.getInt(self.main_win, title, "Decision:", -1, 0, 10000, 1)
        if okPressed:
            return i
        else:
            return 0

    def pass_sequence(self):
        president = self.ui.comboBox_president.currentText()
        chancellor = self.ui.comboBox_chancellor.currentText()

        msg = self.sh.drawThree(president)
        self.ui.label_3.setText(msg)
        option = self.getOption(title="President's Decision")
        deck, msg = self.sh.passTwo(chancellor, option)
        self.ui.label_3.setText(msg)
        option = self.getOption(title="Chancellor's Decision")
        self.sh.deck, played = self.sh.chooseFromTwo(option)

        msg = self.sh.updateGameStatus(played)
        self.ui.label_3.setText(msg)
        
    def reveal_party(self):
        to_player = self.ui.comboBox_president.currentText()
        about_player = self.ui.comboBox_about_player.currentText()
        msg = self.sh.revealParty(to_player, about_player)
        self.ui.label_3.setText(msg)

    def examine(self):
        player = self.ui.comboBox_president.currentText()
        msg = self.sh.examineTopThree(player=player)
        self.ui.label_3.setText(msg)

    def enact(self):
        msg = self.sh.enactTopPolicy()
        self.ui.label_3.setText(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())