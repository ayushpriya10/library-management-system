import sys
from pymongo import MongoClient
import re
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from UI_Files.startScreen import Ui_LoginScreen
from UI_Files.reportScreen import Ui_reportScreen
from UI_Files.issueScreen import Ui_issueScreen
from UI_Files.bookSearchScreen import Ui_BookSearch
from UI_Files.bookFormScreen import Ui_BookForm

def messageBox(self, flag):
    if flag == 1:
        return QMessageBox.about(self, "Login Error", "The credentials entered are incorrect! Please try again!")
    if flag == 2:
        return QMessageBox.about(self, "Login Error", "Please enter both username and password and try again.")
    if flag == 3:
        return QMessageBox.about(self, "Incomplete Details", "Please fill all three fields to issue book(s).")
    if flag == 4:
        return QMessageBox.about(self, "Incomplete Details", "Please fill all three fields to return book(s).")
    if flag == 5:
        return QMessageBox.critical(self, "Delete Record", "Are you sure you want to delete the record for this book?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if flag == 6:
        return QMessageBox.about(self, "Delete Record", "The record has been deleted succesfully.")
    if flag == 7:
        return QMessageBox.about(self, "Error", "Please check the details entered for the book.")
    if flag == 8:
        return QMessageBox.about(self, "Saved", "The record was succesfully saved.")

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)
        self.adminCollection = MongoClient("mongodb://localhost:27017/")["lms"]["admins"]
        self.bookCollection = MongoClient("mongodb://localhost:27017/")["lms"]["books"]
        self.empCollection = MongoClient("mongodb://localhost:27017/")["lms"]["emp"]
        self.updateRec = False
        self.id = None


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
            self.ui.searchBooksBtn.clicked.connect(self.searchBooksWin)
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

    def searchBooksWin(self):
        self.close()
        self.ui = Ui_BookSearch()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.back)
        self.ui.searchStr.textEdited.connect(self.searchBooks)
        self.ui.editBtn.clicked.connect(self.editBook)
        for i in self.bookCollection.find():
            if i["noc"] > -1:
                self.ui.listWidget.addItem(i["name"] + " " + i["code"])
        self.show()

    def editBook(self):
        item = self.ui.listWidget.currentItem().text().split(" ")

        # print(item[len(item)-1])
        record = self.bookCollection.find_one({"code":item[len(item)-1]})
        # print(record)
        self.close()
        self.ui = Ui_BookForm()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.back)
        self.ui.delBtn.clicked.connect(self.delRecord)
        self.ui.saveBtn.clicked.connect(self.saveRecord)
        self.ui.nameText.setText(record["name"])
        self.ui.pubText.setText(record["publisher"])
        self.ui.authText.setText(record["author"])
        self.ui.nocText.setText(str(record["noc"]))
        self.ui.codeText.setText(record["code"])
        self.ui.costText.setText(record["cost"])
        self.id = self.bookCollection.find_one({"code":record["code"]})["_id"]
        self.updateRec = True
        self.show()

    def saveRecord(self):
        code = self.ui.codeText.text().upper()
        name = self.ui.nameText.text()
        publisher = self.ui.pubText.text()
        author = self.ui.authText.text()
        noc = self.ui.nocText.text()
        cost = self.ui.costText.text()
        # print(code)
        if self.updateRec and self.validateBookForm():
            self.updateRec = False
            self.bookCollection.update({"_id":self.id}, {'$set':{"name":name, "code":code, "publisher": publisher, "author":author, "noc":int(noc), "cost":cost, "issueID":""}})
            # print(self.bookCollection.find_one({"code":code})["_id"])
            messageBox(self, 8)
            self.back()
        elif self.updateRec == False and self.bookCollection.find_one({"code":code}) and self.validateBookForm():
            self.bookCollection.insert({"name":name, "code":code, "publisher": publisher, "author":author, "noc":int(noc), "cost":cost, "issueID":""})
            messageBox(self, 8)
            self.back()
        else:
            messageBox(self, 7)

    def validateBookForm(self):
        flag = True

        code = self.ui.codeText.text().upper()
        name = self.ui.nameText.text()
        publisher = self.ui.pubText.text()
        author = self.ui.authText.text()
        noc = self.ui.nocText.text()
        cost = self.ui.costText.text()

        codePat = re.compile(r'^\w\d{3}$')
        if not bool(re.match(codePat, code)):
            flag = False
            print("code failed")

        namePat = re.compile(r'\w+')
        if len(name) < 5: #not bool(re.match(namePat, name)):
            flag = False
            print("name failed")

        if len(publisher) < 1:
            flag = False
            print("pub failed")

        if len(author) < 1:
            flag = False
            print("auth failed")

        nocPat = re.compile(r'^\d+$')
        if ((not bool(re.match(nocPat, str(noc)))) and noc < 0):
            flag = False
            print("noc failed")

        costPat = re.compile(r'^\d+$')
        if ((not bool(re.match(costPat, cost))) and float(cost) < 1):
            flag = False
            print("cost failed")

        return flag

    def delRecord(self):
        code = self.ui.codeText.text()
        # print(QMessageBox.Yes == messageBox(self, 5))
        # print(code)
        if QMessageBox.Yes == messageBox(self, 5):
            # print("true")
            self.bookCollection.remove({"code":code})
            messageBox(self, 6)
            self.back()
        # else:
        #     print("false")

    def searchBooks(self):
        # print(self.ui.searchStr.text())
        # print(self.ui.comboBox.currentText())
        searchStr = self.ui.searchStr.text()
        cat = self.ui.comboBox.currentText()
        self.ui.listWidget.clear()

        if searchStr == "":
            for i in self.bookCollection.find():
                if i["noc"] > -1:
                    self.ui.listWidget.addItem(i["name"])

        for i in self.bookCollection.find():
            # print(cat.lower()[0], i["code"], searchStr.lower(), i["name"])

            if cat[0] in i["code"] and searchStr.lower() in i["name"].lower():
                # print(cat.lower()[0], i["code"], searchStr.lower(), i["name"])
                self.ui.listWidget.addItem(i["name"])

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
        self.ui.searchBooksBtn.clicked.connect(self.searchBooksWin)
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
