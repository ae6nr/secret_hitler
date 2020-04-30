# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'playerwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.player_table = QtWidgets.QTableView(Form)
        self.player_table.setGeometry(QtCore.QRect(60, 60, 256, 192))
        self.player_table.setObjectName("player_table")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
