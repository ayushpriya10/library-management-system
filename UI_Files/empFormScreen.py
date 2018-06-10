# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'empFormScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EmpForm(object):
    def setupUi(self, EmpForm):
        EmpForm.setObjectName("EmpForm")
        EmpForm.resize(650, 320)
        EmpForm.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        EmpForm.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(EmpForm)
        self.centralwidget.setObjectName("centralwidget")
        self.nameLbl = QtWidgets.QLabel(self.centralwidget)
        self.nameLbl.setGeometry(QtCore.QRect(20, 25, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nameLbl.setFont(font)
        self.nameLbl.setObjectName("nameLbl")
        self.pinLbl = QtWidgets.QLabel(self.centralwidget)
        self.pinLbl.setGeometry(QtCore.QRect(20, 70, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pinLbl.setFont(font)
        self.pinLbl.setObjectName("pinLbl")
        self.deptLbl = QtWidgets.QLabel(self.centralwidget)
        self.deptLbl.setGeometry(QtCore.QRect(20, 115, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.deptLbl.setFont(font)
        self.deptLbl.setObjectName("deptLbl")
        self.contLbl = QtWidgets.QLabel(self.centralwidget)
        self.contLbl.setGeometry(QtCore.QRect(20, 160, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.contLbl.setFont(font)
        self.contLbl.setObjectName("contLbl")
        self.nameText = QtWidgets.QLineEdit(self.centralwidget)
        self.nameText.setGeometry(QtCore.QRect(220, 28, 400, 30))
        self.nameText.setObjectName("nameText")
        self.deptText = QtWidgets.QLineEdit(self.centralwidget)
        self.deptText.setGeometry(QtCore.QRect(220, 118, 400, 30))
        self.deptText.setObjectName("deptText")
        self.contText = QtWidgets.QLineEdit(self.centralwidget)
        self.contText.setGeometry(QtCore.QRect(220, 163, 400, 30))
        self.contText.setObjectName("contText")
        self.pinText = QtWidgets.QLineEdit(self.centralwidget)
        self.pinText.setGeometry(QtCore.QRect(220, 73, 80, 30))
        self.pinText.setObjectName("pinText")
        self.saveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.saveBtn.setGeometry(QtCore.QRect(300, 220, 100, 35))
        self.saveBtn.setObjectName("saveBtn")
        self.delBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delBtn.setGeometry(QtCore.QRect(410, 220, 100, 35))
        self.delBtn.setObjectName("delBtn")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setGeometry(QtCore.QRect(520, 220, 100, 35))
        self.backBtn.setObjectName("backBtn")
        EmpForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(EmpForm)
        QtCore.QMetaObject.connectSlotsByName(EmpForm)

    def retranslateUi(self, EmpForm):
        _translate = QtCore.QCoreApplication.translate
        EmpForm.setWindowTitle(_translate("EmpForm", "Employee Details"))
        self.nameLbl.setText(_translate("EmpForm", "Name:"))
        self.pinLbl.setText(_translate("EmpForm", "PIN:"))
        self.deptLbl.setText(_translate("EmpForm", "Department:"))
        self.contLbl.setText(_translate("EmpForm", "Contact:"))
        self.saveBtn.setText(_translate("EmpForm", "Save"))
        self.delBtn.setText(_translate("EmpForm", "Delete"))
        self.backBtn.setText(_translate("EmpForm", "Back"))
