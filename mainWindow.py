import sys
from pymongo import MongoClient
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from UI_Files.startScreen import Ui_LoginScreen
from UI_Files.reportScreen import Ui_reportScreen
from UI_Files.issueScreen import Ui_issueScreen

def messageBox(self, flag):
    if flag == 1:
        return QMessageBox.about(self, "Login Error", "The credentials entered are incorrect! Please try again!")
    if flag == 2:
        return QMessageBox.about(self, "Login Error", "Please enter both username and password and try again.")
    if flag == 3:
        return QMessageBox.about(self, "Incomplete Details", "Please fill all three fields to issue book(s).")
    if flag == 4:
        return QMessageBox.about(self, "Incomplete Details", "Please fill all three fields to return book(s).")

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)
        self.adminCollection = MongoClient("mongodb://localhost:27017/")["lms"]["admins"]

    def login(self):
        uname = self.ui.unameText.text()
        passwd = self.ui.passText.text()

        if self.adminCollection.find_one({"username": uname, "password": passwd}):
            self.close()
            self.ui = Ui_issueScreen()
            self.ui.setupUi(self)
            self.ui.logout.clicked.connect(self.logout)
            self.ui.generateReportBtn.clicked.connect(self.report)
            self.ui.issueBookBtn.clicked.connect(self.issueBooks)
            self.ui.editBookDetails.clicked.connect(self.editBookDetails)
            self.ui.editEmpDetails.clicked.connect(self.editEmployeeDetails)
            self.ui.searchBooksBtn.clicked.connect(self.searchBooks)
            self.ui.returnBookBtn.clicked.connect(self.returnBooks)
            self.show()
        elif uname == "" or passwd == "":
            messageBox(self, 2)
            self.ui.unameText.setText("")
            self.ui.passText.setText("")
        else:
            messageBox(self, 1)
            self.ui.unameText.setText("")
            self.ui.passText.setText("")

    def logout(self):
        self.close()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)
        self.show()

    def editBookDetails(self):
        print("Edit Book Details")

    def editEmployeeDetails(self):
        print("Edit Employee Details")

    def searchBooks(self):
        print("Search Books")

    def issueBooks(self):
        book1 = self.ui.book1Text.text()
        book2 = self.ui.book2Text.text()
        empPIN = self.ui.empPinText.text()

        if book1 and book2 and empPIN:
            print(book1, book2, empPIN)
        else:
            messageBox(self, 3)
            self.ui.book1Text.setText("")
            self.ui.book2Text.setText("")
            self.ui.empPinText.setText("")

    def returnBooks(self):
        book1 = self.ui.book1Text.text()
        book2 = self.ui.book2Text.text()
        empPIN = self.ui.empPinText.text()

        if book1 and book2 and empPIN:
            print(book1, book2, empPIN)
        else:
            messageBox(self, 4)
            self.ui.book1Text.setText("")
            self.ui.book2Text.setText("")
            self.ui.empPinText.setText("")

    def back(self):
        self.close()
        self.ui = Ui_issueScreen()
        self.ui.setupUi(self)
        self.ui.logout.clicked.connect(self.logout)
        self.ui.generateReportBtn.clicked.connect(self.report)
        self.ui.issueBookBtn.clicked.connect(self.issueBooks)
        self.ui.editBookDetails.clicked.connect(self.editBookDetails)
        self.ui.editEmpDetails.clicked.connect(self.editEmployeeDetails)
        self.ui.searchBooksBtn.clicked.connect(self.searchBooks)
        self.ui.returnBookBtn.clicked.connect(self.returnBooks)
        self.show()

    def report(self):
        self.close()
        self.ui = Ui_reportScreen()
        self.ui.setupUi(self)
        self.ui.back.clicked.connect(self.back)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
