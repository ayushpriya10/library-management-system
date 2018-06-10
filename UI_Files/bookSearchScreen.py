# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookSearchScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BookSearch(object):
    def setupUi(self, BookSearch):
        BookSearch.setObjectName("BookSearch")
        BookSearch.resize(760, 640)
        BookSearch.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        BookSearch.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(BookSearch)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(600, 28, 130, 35))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.searchStr = QtWidgets.QLineEdit(self.centralwidget)
        self.searchStr.setGeometry(QtCore.QRect(20, 75, 710, 35))
        self.searchStr.setObjectName("searchStr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 25, 570, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 130, 710, 400))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setAlternatingRowColors (True)
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(500, 550, 100, 35))
        self.editBtn.setObjectName("editBtn")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(630, 550, 100, 35))
        self.backBtn.setObjectName("backBtn")
        BookSearch.setCentralWidget(self.centralwidget)

        self.retranslateUi(BookSearch)
        QtCore.QMetaObject.connectSlotsByName(BookSearch)

    def retranslateUi(self, BookSearch):
        _translate = QtCore.QCoreApplication.translate
        BookSearch.setWindowTitle(_translate("BookSearch", "Search Books"))
        self.comboBox.setItemText(0, _translate("BookSearch", "General"))
        self.comboBox.setItemText(1, _translate("BookSearch", "Technical"))
        self.comboBox.setItemText(2, _translate("BookSearch", "Management"))
        self.comboBox.setItemText(3, _translate("BookSearch", "Finance"))
        self.label.setText(_translate("BookSearch", "Please select search type before proceeding:"))
        self.editBtn.setText(_translate("BookSearch", "Edit"))
        self.backBtn.setText(_translate("BookSearch", "Go Back"))
