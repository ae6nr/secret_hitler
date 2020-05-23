# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emailsettingswindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(416, 223)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/sh/Secret-Hitler.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(230, 99, 66);")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_email = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_email.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_email.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_email.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout.addWidget(self.lineEdit_email)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_password.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_password.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.lineEdit_invite_link = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_invite_link.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEdit_invite_link.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lineEdit_invite_link.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_invite_link.setObjectName("lineEdit_invite_link")
        self.horizontalLayout_4.addWidget(self.lineEdit_invite_link)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 3)
        spacerItem3 = QtWidgets.QSpacerItem(152, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 0, 1, 1)
        self.radioButton_send = QtWidgets.QRadioButton(Dialog)
        self.radioButton_send.setChecked(False)
        self.radioButton_send.setObjectName("radioButton_send")
        self.gridLayout.addWidget(self.radioButton_send, 3, 1, 1, 1)
        self.radioButton_dont_send = QtWidgets.QRadioButton(Dialog)
        self.radioButton_dont_send.setChecked(True)
        self.radioButton_dont_send.setObjectName("radioButton_dont_send")
        self.gridLayout.addWidget(self.radioButton_dont_send, 3, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(391, 35, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_start_new_game = QtWidgets.QPushButton(Dialog)
        self.pushButton_start_new_game.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_start_new_game.setObjectName("pushButton_start_new_game")
        self.horizontalLayout_3.addWidget(self.pushButton_start_new_game)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.gridLayout.addLayout(self.horizontalLayout_3, 5, 0, 1, 3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Email Settings"))
        self.label.setText(_translate("Dialog", "Email Address"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "Video Call Link"))
        self.radioButton_send.setText(_translate("Dialog", "Send Emails"))
        self.radioButton_dont_send.setText(_translate("Dialog", "Don\'t Send Emails"))
        self.pushButton_start_new_game.setText(_translate("Dialog", "Start New Game"))
        self.pushButton_save.setText(_translate("Dialog", "Save"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
import sh_rc
