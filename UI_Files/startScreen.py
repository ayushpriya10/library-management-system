# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginScreen(object):
    def setupUi(self, LoginScreen):
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(710, 250)
        LoginScreen.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        LoginScreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(LoginScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 700, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(570, 180, 100, 50))
        self.loginButton.setObjectName("loginButton")
        self.passText = QtWidgets.QLineEdit(self.centralwidget)#.Password
        self.passText.setGeometry(QtCore.QRect(170, 130, 500, 35))
        self.passText.setObjectName("passText")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 150, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.unameText = QtWidgets.QLineEdit(self.centralwidget)
        self.unameText.setGeometry(QtCore.QRect(170, 80, 500, 35))
        self.unameText.setObjectName("unameText")
        LoginScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginScreen)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)

    def retranslateUi(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "Login"))
        self.label.setText(_translate("LoginScreen", "Welcome! Please Login to Continue."))
        self.loginButton.setText(_translate("LoginScreen", "Login"))
        self.label_2.setText(_translate("LoginScreen", "Password:"))
        self.label_3.setText(_translate("LoginScreen", "Username:"))
