# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminFormScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_adminForm(object):
    def setupUi(self, adminForm):
        adminForm.setObjectName("adminForm")
        adminForm.resize(525, 260)
        adminForm.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        adminForm.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(adminForm)
        self.centralwidget.setObjectName("centralwidget")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(280, 160, 100, 35))
        self.saveBtn.setObjectName("saveBtn")
        self.passText = QtWidgets.QLineEdit(self.centralwidget)
        self.passText.setGeometry(QtCore.QRect(210, 73, 280, 30))
        self.passText.setObjectName("passText")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 25, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.unameText = QtWidgets.QLineEdit(self.centralwidget)
        self.unameText.setGeometry(QtCore.QRect(210, 28, 280, 30))
        self.unameText.setObjectName("unameText")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 115, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.passConfText = QtWidgets.QLineEdit(self.centralwidget)
        self.passConfText.setGeometry(QtCore.QRect(210, 118, 280, 30))
        self.passConfText.setObjectName("passConfText")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(390, 160, 100, 35))
        self.backBtn.setObjectName("backBtn")
        adminForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(adminForm)
        QtCore.QMetaObject.connectSlotsByName(adminForm)

    def retranslateUi(self, adminForm):
        _translate = QtCore.QCoreApplication.translate
        adminForm.setWindowTitle(_translate("adminForm", "Add Admin"))
        self.saveBtn.setText(_translate("adminForm", "Add"))
        self.label_2.setText(_translate("adminForm", "Password:"))
        self.label_3.setText(_translate("adminForm", "Username:"))
        self.label_4.setText(_translate("adminForm", "Confirm Pass:"))
        self.backBtn.setText(_translate("adminForm", "Back"))
