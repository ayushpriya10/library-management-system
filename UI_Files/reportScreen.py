# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainScreen.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_reportScreen(object):
    def setupUi(self, mainScreen):
        mainScreen.setObjectName("mainScreen")
        mainScreen.resize(600, 380)
        mainScreen.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        mainScreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.reportTitleLabel = QtWidgets.QLabel(self.centralwidget)
        self.reportTitleLabel.setGeometry(QtCore.QRect(30, 20, 400, 60))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.reportTitleLabel.setFont(font)
        self.reportTitleLabel.setObjectName("reportTitleLabel")
        self.bookReportLabel = QtWidgets.QLabel(self.centralwidget)
        self.bookReportLabel.setGeometry(QtCore.QRect(40, 100, 400, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bookReportLabel.setFont(font)
        self.bookReportLabel.setObjectName("bookReportLabel")
        self.empReportLabel = QtWidgets.QLabel(self.centralwidget)
        self.empReportLabel.setGeometry(QtCore.QRect(40, 150, 400, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.empReportLabel.setFont(font)
        self.empReportLabel.setObjectName("empReportLabel")
        self.generateBookReport = QtWidgets.QPushButton(self.centralwidget)
        self.generateBookReport.setGeometry(QtCore.QRect(440, 100, 130, 35))
        self.generateBookReport.setObjectName("generateBookReport")
        self.generateEmpReport = QtWidgets.QPushButton(self.centralwidget)
        self.generateEmpReport.setGeometry(QtCore.QRect(440, 150, 130, 35))
        self.generateEmpReport.setObjectName("generateEmpReport")
        self.overallReportLabel = QtWidgets.QLabel(self.centralwidget)
        self.overallReportLabel.setGeometry(QtCore.QRect(40, 200, 400, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.overallReportLabel.setFont(font)
        self.overallReportLabel.setObjectName("overallReportLabel")
        self.generateOverallReport = QtWidgets.QPushButton(self.centralwidget)
        self.generateOverallReport.setGeometry(QtCore.QRect(440, 200, 130, 35))
        self.generateOverallReport.setObjectName("generateOverallReport")
        self.bookDetailsLabel = QtWidgets.QLabel(self.centralwidget)
        self.bookDetailsLabel.setGeometry(QtCore.QRect(40, 250, 400, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bookDetailsLabel.setFont(font)
        self.bookDetailsLabel.setObjectName("bookDetailsLabel")
        self.generateBookDetail = QtWidgets.QPushButton(self.centralwidget)
        self.generateBookDetail.setGeometry(QtCore.QRect(440, 250, 130, 35))
        self.generateBookDetail.setObjectName("generateBookDetail")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(440, 300, 130, 35))
        self.back.setObjectName("back")
        mainScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainScreen)
        QtCore.QMetaObject.connectSlotsByName(mainScreen)

    def retranslateUi(self, mainScreen):
        _translate = QtCore.QCoreApplication.translate
        mainScreen.setWindowTitle(_translate("mainScreen", "LMS Workspace"))
        self.reportTitleLabel.setText(_translate("mainScreen", "Report generation"))
        self.bookReportLabel.setText(_translate("mainScreen", "Frequently issued Books:"))
        self.empReportLabel.setText(_translate("mainScreen", "Frequently issuing Employees:"))
        self.generateBookReport.setText(_translate("mainScreen", "Generate"))
        self.generateEmpReport.setText(_translate("mainScreen", "Generate"))
        self.overallReportLabel.setText(_translate("mainScreen", "Overall Employee Report:"))
        self.generateOverallReport.setText(_translate("mainScreen", "Generate"))
        self.bookDetailsLabel.setText(_translate("mainScreen", "Overall Book Report:"))
        self.generateBookDetail.setText(_translate("mainScreen", "Generate"))
        self.back.setText(_translate("mainScreen", "Go Back"))
