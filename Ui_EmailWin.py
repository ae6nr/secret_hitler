# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'emailsettingswindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(418, 243)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(11, 11, 396, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_email = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.horizontalLayout.addWidget(self.lineEdit_email)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_invite_link = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_invite_link.setObjectName("lineEdit_invite_link")
        self.horizontalLayout_4.addWidget(self.lineEdit_invite_link)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.radioButton_send = QtWidgets.QRadioButton(self.widget)
        self.radioButton_send.setChecked(False)
        self.radioButton_send.setObjectName("radioButton_send")
        self.verticalLayout.addWidget(self.radioButton_send)
        self.radioButton_dont_send = QtWidgets.QRadioButton(self.widget)
        self.radioButton_dont_send.setChecked(True)
        self.radioButton_dont_send.setObjectName("radioButton_dont_send")
        self.verticalLayout.addWidget(self.radioButton_dont_send)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_start_new_game = QtWidgets.QPushButton(self.widget)
        self.pushButton_start_new_game.setObjectName("pushButton_start_new_game")
        self.horizontalLayout_3.addWidget(self.pushButton_start_new_game)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_save = QtWidgets.QPushButton(self.widget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_3.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_3.addWidget(self.pushButton_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Email Address"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "Video Call Link"))
        self.radioButton_send.setText(_translate("Dialog", "Send Emails"))
        self.radioButton_dont_send.setText(_translate("Dialog", "Don\'t Send Emails"))
        self.pushButton_start_new_game.setText(_translate("Dialog", "Start New Game"))
        self.pushButton_save.setText(_translate("Dialog", "Save"))
        self.pushButton_cancel.setText(_translate("Dialog", "Cancel"))
