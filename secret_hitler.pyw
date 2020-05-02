#
#
#
# pyuic5 mainwindow.ui -o Ui_MainWin.py
# pyuic5 playerwindow.ui -o Ui_PlayerWin.py
# pyuic5 emailsettingswindow.ui -o Ui_EmailWin.py

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QInputDialog, QDialog, QMessageBox

import PyQt5
from Ui_MainWin import Ui_MainWindow
from Ui_PlayerWin import Ui_Dialog as Ui_Dialog_PlayerWin
from Ui_EmailWin import Ui_Dialog as Ui_Dialog_EmailWin
from SecretHitler import SecretHitler

class EmailWindow:
    def __init__(self, main, email, password, invite_link):
        self.main = main
        self.dlg = QDialog()
        self.ui = Ui_Dialog_EmailWin()
        self.ui.setupUi(self.dlg)

        self.ui.lineEdit_email.setText(email)
        self.ui.lineEdit_password.setText(password)
        self.ui.lineEdit_invite_link.setText(invite_link)

        self.ui.pushButton_save.clicked.connect(self.save)
        self.ui.pushButton_cancel.clicked.connect(self.cancel)
        self.ui.pushButton_start_new_game.clicked.connect(self.start_game)

    def updateEmailPref(self):
        if self.ui.radioButton_send.isChecked():
            self.main.send_emails = True
            self.main.ui.statusbar.showMessage("Sending emails, huh?")
        else:
            self.main.send_emails = False
            self.main.ui.statusbar.showMessage("No emails will be sent.")


    def save(self):
        self.main.sender_email = self.ui.lineEdit_email.text()
        self.main.sender_email_password = self.ui.lineEdit_password.text()
        self.main.invite_link = self.ui.lineEdit_invite_link.text()
        self.updateEmailPref()
        self.dlg.close()

    def cancel(self):
        self.main.ui.statusbar.showMessage("Settings not saved.")
        self.dlg.close()

    def start_game(self):
        self.save()
        self.main.startNewGame()
        self.dlg.close()
    

class PlayerWindow:
    def __init__(self, main, current_emails):
        self.main = main
        self.dlg = QDialog()
        self.ui = Ui_Dialog_PlayerWin()
        self.ui.setupUi(self.dlg)

        i = 0
        for name in current_emails:
            self.ui.tableWidget.item(i, 0).setText(name)
            self.ui.tableWidget.item(i, 1).setText(current_emails[name])
            i += 1

        self.ui.pushButton.clicked.connect(self.updatePlayers)
    
    def updatePlayers(self):

        newDict = {}

        for i in range(0,10):
            name = self.ui.tableWidget.item(i, 0).text()
            email = self.ui.tableWidget.item(i, 1).text()
            if name != '' and email != '':
                newDict[name] = email

        self.main.updatedDictionary = newDict

        for i in range(0,10):
            self.ui.tableWidget.item(i, 0).setText("")
            self.ui.tableWidget.item(i, 1).setText("")

        i = 0
        for name in self.main.updatedDictionary:
            self.ui.tableWidget.item(i, 0).setText(name)
            self.ui.tableWidget.item(i, 1).setText(self.main.updatedDictionary[name])
            i += 1

        #self.dlg.close()

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
        self.updatedDictionary = self.emaildict

        self.send_emails = False
        self.invite_link = ""

        self.startNewGame()
        self.updatePresInfo()

        # Connect signals to slots
        self.ui.pushButton_pass.clicked.connect(self.pass_sequence)
        self.ui.pushButton_reveal.clicked.connect(self.reveal_party)
        self.ui.pushButton_examine.clicked.connect(self.examine)
        self.ui.pushButton_enact.clicked.connect(self.enact)
        self.ui.actionStart_New_Game.triggered.connect(self.startNewGame)
        self.ui.actionPlayer_Settings.triggered.connect(self.updatePlayers)
        self.ui.comboBox_president.currentIndexChanged.connect(self.updatePresInfo)
        self.ui.actionAdd_Sender_Email.triggered.connect(self.emailSettings)

    def show(self):
        self.main_win.show()

    def emailSettings(self):
        pop = EmailWindow(self, self.sender_email, self.sender_email_password, self.invite_link)
        pop.dlg.exec_()

    def updatePlayers(self):
        pop = PlayerWindow(self, self.updatedDictionary)
        pop.dlg.exec_()

    def updatePresInfo(self):
        msg = self.ui.comboBox_president.currentText() + " is the president."
        self.ui.statusbar.showMessage(msg)
        self.ui.label_pres_info_1.setText(msg)
        self.ui.label_pres_info_2.setText(msg)

    def startNewGame(self):

        if self.send_emails:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setWindowTitle("Email confirmation")
            msg.setText("Are you sure you want to send emails?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                
            retval = msg.exec_()
            if retval == QMessageBox.Ok:
                self.ui.statusbar.showMessage("Sending emails...")
            else:
                self.ui.statusbar.showMessage("No emails were sent.")
                return

        self.emaildict = self.updatedDictionary

        i = 0
        for name in self.emaildict:
            self.ui.comboBox_president.setItemText(i, name)
            self.ui.comboBox_chancellor.setItemText(i, name)
            self.ui.comboBox_about_player.setItemText(i, name)
            i += 1

        for j in range(i, 11):
            name = '...'
            self.ui.comboBox_president.setItemText(j, name)
            self.ui.comboBox_chancellor.setItemText(j, name)
            self.ui.comboBox_about_player.setItemText(j, name)

        self.sh = SecretHitler(self.emaildict, self.sender_email, self.sender_email_password, sendemails=self.send_emails, invite_link=self.invite_link) # To actually send emails, set sendemails=True
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

        try:
            self.emaildict[president]
            self.emaildict[chancellor]
        except:
            self.ui.label_3.setText("You chose an invalid name.")
            return

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