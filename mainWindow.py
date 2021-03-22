import sys
from pymongo import MongoClient
import re
import datetime
from os import system
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from UI_Files.startScreen import Ui_LoginScreen
from UI_Files.reportScreen import Ui_reportScreen
from UI_Files.issueScreen import Ui_issueScreen
from UI_Files.bookSearchScreen import Ui_BookSearch
from UI_Files.bookFormScreen import Ui_BookForm
from UI_Files.empFormScreen import Ui_EmpForm
from UI_Files.adminFormScreen import Ui_adminForm

def messageBox(self, flag):
    if flag == 1:
        return QMessageBox.about(self, "Login Error", "The credentials entered are incorrect! Please try again!")
    if flag == 2:
        return QMessageBox.about(self, "Login Error", "Please enter both username and password and try again.")
    if flag == 3:
        return QMessageBox.about(self, "Incomplete Details", "Please fill all three fields correctly to issue book(s).")
    if flag == 4:
        return QMessageBox.about(self, "Incomplete Details", "Please fill all three fields correctly to return book(s).")
    if flag == 5:
        return QMessageBox.critical(self, "Delete Record", "Are you sure you want to delete this record?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    if flag == 6:
        return QMessageBox.about(self, "Delete Record", "The record has been deleted succesfully.")
    if flag == 7:
        return QMessageBox.about(self, "Error", "Please check the details entered.")
    if flag == 8:
        return QMessageBox.about(self, "Saved", "The record was succesfully saved.")
    if flag == 9:
        return QMessageBox.about(self, "Code Error", "Please check the code entered for the book and try again.")
    if flag == 10:
        return QMessageBox.about(self, "Code Error", "Please check the code entered for the employee and try again.")
    if flag == 11:
        return QMessageBox.about(self, "Error", "No record found. Please check the details entered.")
    if flag == 12:
        return QMessageBox.about(self, "Error", "Sorry, the username already exists. Please try with a different one.")
    if flag == 13:
        return QMessageBox.about(self, "Error", "The passwords don't match. Please try again.")
    if flag == 14:
        return QMessageBox.about(self, "Book Issue", "The books are issued succesfully.")
    if flag == 15:
        return QMessageBox.about(self, "Book Issue Error", "The employee already has issued books.")
    if flag == 16:
        return QMessageBox.about(self, "Not Found", "Employee not found! Try again.")
    if flag == 17:
        return QMessageBox.about(self, "Not Found", "Book not found. Please try again.")
    if flag == 18:
        return QMessageBox.about(self, "Unavailable", "Book not available.")
    if flag == 19:
        return QMessageBox.about(self, "No Books Issued", "The employee doesn't have any books issued.")
    if flag == 20:
        return QMessageBox.about(self, "Book Issue", "The books are returned succesfully.")
    if flag == 21:
        return QMessageBox.about(self, "Report Generation", "Report was generated succesfully.")

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)
        self.adminCollection = MongoClient("mongodb://localhost:27017/")["lms"]["admins"]
        self.bookCollection = MongoClient("mongodb://localhost:27017/")["lms"]["books"]
        self.empCollection = MongoClient("mongodb://localhost:27017/")["lms"]["emp"]
        self.issuedCollection = MongoClient("mongodb://localhost:27017/")["lms"]["issued"]
        self.updateRec = False
        self.id = None

    def printTest(self):
        print("Test Passed.")

    def login(self):
        uname = self.ui.unameText.text()
        passwd = self.ui.passText.text()

        if self.adminCollection.find_one({"username": uname, "password": passwd}):
            self.close()
            self.ui = Ui_issueScreen()
            self.ui.setupUi(self)
            self.ui.actionAdd_New_Employee.triggered.connect(self.addNewEmp)
            self.ui.actionAdd_New_Book.triggered.connect(self.addNewBook)
            self.ui.actionAdd_New_Admin.triggered.connect(self.addNewAdmin)
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

    def addNewEmp(self):
        self.close()
        self.ui = Ui_EmpForm()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.back)
        self.ui.delBtn.clicked.connect(self.delEmpRecord)
        self.ui.saveBtn.clicked.connect(self.saveEmpRecord)
        self.updateRec = False
        self.show()

    def addNewBook(self):
        self.close()
        self.ui = Ui_BookForm()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.back)
        self.ui.delBtn.clicked.connect(self.delRecord)
        self.ui.saveBtn.clicked.connect(self.saveRecord)
        self.show()

    def addNewAdmin(self):
        # print("add new admin")
        self.close()
        self.ui = Ui_adminForm()
        self.ui.setupUi(self)
        self.ui.backBtn.clicked.connect(self.back)
        self.ui.saveBtn.clicked.connect(self.saveAdmin)
        self.show()

    def saveAdmin(self):
        uname = self.ui.unameText.text()
        passwd = self.ui.passText.text()
        passwdConf = self.ui.passConfText.text()

        if passwdConf == passwd:
            if self.adminCollection.find_one({"username":uname}):
                messageBox(self, 12)
            else:
                self.adminCollection.insert({"username":uname, "password":passwd})
                messageBox(self, 8)
                self.back()
        else:
            messageBox(self, 13)

    def logout(self):
        self.close()
        self.ui = Ui_LoginScreen()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)
        self.show()

    def editBookDetails(self):
        code = self.ui.bookEditText.text().upper()

        if bool(re.match(r'^\w\d{3}$', code)):
            record = self.bookCollection.find_one({"code":code})
            if not(record):
                messageBox(self, 11)
            else:
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
        else:
            messageBox(self, 9)

    def editEmployeeDetails(self):
        # print("Edit Employee Details")
        pin = self.ui.editEmpText.text()

        if bool(re.match(r'^\d{5}$', pin)):
            record = self.empCollection.find_one({"PIN":pin})
            if not(record):
                messageBox(self, 11)
            else:
                self.close()
                self.ui = Ui_EmpForm()
                self.ui.setupUi(self)
                self.ui.backBtn.clicked.connect(self.back)
                self.ui.delBtn.clicked.connect(self.delEmpRecord)
                self.ui.saveBtn.clicked.connect(self.saveEmpRecord)
                self.ui.nameText.setText(record["name"])
                self.ui.deptText.setText(record["dept"])
                self.ui.contText.setText(record["contact"])
                self.ui.pinText.setText(record["PIN"])
                self.id = self.empCollection.find_one({"PIN":pin})["_id"]
                self.updateRec = True
                self.show()
        else:
            messageBox(self, 10)

    def saveEmpRecord(self):
        pin = self.ui.pinText.text()
        name = self.ui.nameText.text()
        dept = self.ui.deptText.text()
        contact = self.ui.contText.text()

        if self.updateRec and self.validateEmpForm():
            self.updateRec = False
            self.empCollection.update({"_id":self.id}, {'$set':{"name":name, "PIN":pin, "dept": dept, "contact":contact, "issueID":""}})
            # print(self.bookCollection.find_one({"code":code})["_id"])
            messageBox(self, 8)
            self.id = None
            # print("update")
            self.back()
        elif self.updateRec == False and self.validateEmpForm():
            self.empCollection.insert({"name":name, "PIN":pin, "dept": dept, "contact":contact, "issueID":""})
            messageBox(self, 8)
            # print("add new")
            self.back()
        else:
            messageBox(self, 7)

    def validateEmpForm(self):
        flag = True

        pin = self.ui.pinText.text()
        name = self.ui.nameText.text()
        dept = self.ui.deptText.text()
        contact = self.ui.contText.text()

        pinPat = re.compile(r'^\d{5}$')
        if not bool(re.match(pinPat, pin)):
            print("pin failed", pin)
            flag = False

        contactPat = re.compile(r'^\d{10}$')
        if not bool(re.match(contactPat, contact)):
            print("contact failed", len(contact))
            flag = False

        if len(name) < 1: #not bool(re.match(namePat, name)):
            flag = False
            print("name failed")

        if len(dept) < 4:
            flag = False
            print("dept failed")

        return flag

    def delEmpRecord(self):
        pin = self.ui.pinText.text()
        # print(QMessageBox.Yes == messageBox(self, 5))
        # print(code)
        if QMessageBox.Yes == messageBox(self, 5):
            # print("true")
            self.bookCollection.remove({"PIN":pin})
            messageBox(self, 6)
            self.back()

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
            self.id = None
            self.back()
        elif self.updateRec == False and not(self.bookCollection.find_one({"code":code})) and self.validateBookForm():
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
        book1 = self.ui.book1Text.text().upper()
        book2 = self.ui.book2Text.text().upper()
        empPIN = self.ui.empPinText.text()
        today = datetime.date.today()

        if bool(re.match(r"^\w\d{3}$", book1.upper())) and bool(re.match(r"^\w\d{3}$", book2.upper())) and bool(re.match(r"^\d{5}$", empPIN)) and not(book1 == book2):
            # print(book1, book2, empPIN)
            emp = self.empCollection.find_one({"PIN":empPIN})
            b1 = self.bookCollection.find_one({"code":book1})
            b2 = self.bookCollection.find_one({"code":book2})

            if emp != None:
                if emp["issueID"] == "":
                    empID = emp["_id"]
                    if b1 != None or b2 != None and b1 != b2:
                        if b1["noc"] > 0 and b2["noc"] > 0:
                            self.issuedCollection.insert({"book1":book1, "book2":book2, "PIN":empPIN, "issueDate":str(today), "returnDate":str(today + datetime.timedelta(15)), "actualReturnDate":"", "fine":"", "fineDue":False})
                            record = self.issuedCollection.find_one({"book1":book1, "book2":book2, "PIN":empPIN})
                            self.empCollection.update({"_id":empID}, {'$set':{"name":emp["name"], "PIN":emp["PIN"], "dept": emp["dept"], "contact":emp["contact"], "issueID":record["_id"]}})
                            cost1 = b1['cost']
                            cost2 = b2['cost']
                            self.bookCollection.update({"_id":b1["_id"]}, {'$set':{"name":b1["name"], "code":b1["code"], "publisher": b1["publisher"], "author":b1["author"], "noc":b1["noc"]-1, "cost":cost1, "issueID":record["_id"]}})
                            self.bookCollection.update({"_id":b2["_id"]}, {'$set':{"name":b2["name"], "code":b2["code"], "publisher": b2["publisher"], "author":b2["author"], "noc":b2["noc"]-1, "cost":cost2, "issueID":record["_id"]}})
                            messageBox(self, 14)
                            self.ui.book1Text.setText("")
                            self.ui.book2Text.setText("")
                            self.ui.empPinText.setText("")
                        else:
                            messageBox(self, 18)
                    else:
                        messageBox(self, 17)
                else:
                    messageBox(self, 15)
            else:
                messageBox(self, 16)
        else:
            messageBox(self, 3)

    def returnBooks(self):
        book1 = self.ui.book1Text.text().upper()
        book2 = self.ui.book2Text.text().upper()
        empPIN = self.ui.empPinText.text()
        today = datetime.date.today()

        if bool(re.match(r"^\w\d{3}$", book1.upper())) and bool(re.match(r"^\w\d{3}$", book2.upper())) and bool(re.match(r"^\d{5}$", empPIN)) and not(book1 == book2):
            # print(book1, book2, empPIN)
            emp = self.empCollection.find_one({"PIN":empPIN})
            b1 = self.bookCollection.find_one({"code":book1})
            b2 = self.bookCollection.find_one({"code":book2})

            if emp != None:
                if emp["issueID"] != "":
                    empID = emp["_id"]
                    if b1 != None and b2 != None and b1 != b2:
                        record = self.issuedCollection.find_one({"book1":book1, "book2":book2, "PIN":empPIN})
                        year, month, day = [int(i) for i in record["returnDate"].split("-")]
                        t = datetime.date(year, month, day)

                        if (today-t).days < 1:
                            flag = False
                            amount = ""
                        else:
                            flag = True
                            amount = (today - t).days * 10

                        self.issuedCollection.update({"_id":record["_id"]}, {'$set':{"book1":book1, "book2":book2, "PIN":empPIN, "issueDate":record["issueDate"], "returnDate":record["returnDate"], "actualReturnDate":str(today), "fine":amount, "fineDue":flag}})
                        self.empCollection.update({"_id":empID}, {'$set':{"name":emp["name"], "PIN":emp["PIN"], "dept": emp["dept"], "contact":emp["contact"], "issueID":""}})
                        cost1 = b1['cost']
                        cost2 = b2['cost']
                        self.bookCollection.update({"_id":b1["_id"]}, {'$set':{"name":b1["name"], "code":b1["code"], "publisher": b1["publisher"], "author":b1["author"], "noc":b1["noc"]+1, "cost":cost1, "issueID":""}})
                        self.bookCollection.update({"_id":b2["_id"]}, {'$set':{"name":b2["name"], "code":b2["code"], "publisher": b2["publisher"], "author":b2["author"], "noc":b2["noc"]+1, "cost":cost2, "issueID":""}})
                        messageBox(self, 20)
                        self.ui.book1Text.setText("")
                        self.ui.book2Text.setText("")
                        self.ui.empPinText.setText("")
                    else:
                        messageBox(self, 17)
                else:
                    messageBox(self, 19)
            else:
                messageBox(self, 16)
        else:
            messageBox(self, 4)

    def back(self):
        self.close()
        self.ui = Ui_issueScreen()
        self.ui.setupUi(self)
        self.ui.actionAdd_New_Employee.triggered.connect(self.addNewEmp)
        self.ui.actionAdd_New_Book.triggered.connect(self.addNewBook)
        self.ui.actionAdd_New_Admin.triggered.connect(self.addNewAdmin)
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
        self.ui.generateBookDetail.clicked.connect(self.overallBookReport)
        self.ui.generateOverallReport.clicked.connect(self.overallEmpReport)
        self.ui.generateBookReport.clicked.connect(self.bookStats)
        self.ui.generateEmpReport.clicked.connect(self.empStats)
        self.show()

    def bookStats(self):
        records = self.issuedCollection.find()
        codes = []
        maxCodes = []

        for i in records:
            codes.append(i["book1"])
            codes.append(i["book2"])

        stats = dict()

        for i in codes:
            stats[i] = codes.count(i)

        counts = list(reversed(sorted(list(stats.values()))))
        printStr = "The following books are issued most frequently:"

        while counts:
            for i in codes:
                if i not in maxCodes:
                    if stats[i] == counts[0]:
                        maxCodes.append(i)
                        counts.pop(0)

        for i in maxCodes:
            name = self.bookCollection.find_one({"code":i})["name"]
            printStr += "\n" + str(stats[i]) + "\t" + name

        file = open("topBooks.txt", "w")
        file.write(printStr)
        file.close()
        messageBox(self,21)
        system("notepad topBooks.txt")

    def empStats(self):
        records = self.issuedCollection.find()
        pins = []
        maxPins = []
        for i in records:
            pins.append(i["PIN"])

        stats = dict()

        for i in pins:
            stats[i] = pins.count(i)

        counts = list(reversed(sorted(list(stats.values()))))
        printStr = "The following are the employees who issue books most frequently:"
        while counts:
            for i in pins:
                if i not in maxPins:
                    if stats[i] == counts[0]:
                        maxPins.append(i)
                        counts.pop(0)

        for i in maxPins:
            name = self.empCollection.find_one({"PIN":i})["name"]
            printStr += "\n" + str(stats[i]) + "\t" + name

        file = open("topIssuers.txt", "w")
        file.write(printStr)
        file.close()
        messageBox(self,21)
        system("notepad topIssuers.txt")

    def overallEmpReport(self):
        records = self.empCollection.find()
        printStr = str()
        totalEmp = int()
        totalEmpIssued = int()
        totalDef = int()
        noIssueEmp = "\n\nThe employess who haven't issued any books are as follows:"
        issueEmp = "\n\nThe employess who have issued books are as follows:"
        defaulters = "\n\nThe employees who are yet to pay their fine are as follows:"

        empIssued = []
        for i in self.issuedCollection.find():
            empIssued.append(i["PIN"])
            totalEmpIssued += 1

            if i["fine"] != "" and i["fineDue"]:
                totalDef += 1
                rec = self.empCollection.find_one({"PIN":i["PIN"]})
                defaulters += rec["name"] + "\t" + rec["PIN"]

        for i in records:
            totalEmp += 1
            if i["PIN"] not in empIssued:
                noIssueEmp += "\n" + i["name"] + "\t" + i["PIN"]

        for i in set(empIssued):
            rec = self.empCollection.find_one({"PIN":i})
            issueEmp += "\n" + rec["name"] + "\t" + rec["PIN"]

        printStr = "Total no. of employees: " + str(totalEmp) + "\n\nTotal no. of employess who have issued books: " + str(totalEmpIssued)

        if totalDef > 0:
            printStr += "\n\nTotal no. of defaulters: " + str(totalDef)

            printStr += defaulters

        printStr += issueEmp + noIssueEmp
        file = open("overallEmpReport.txt" , "w")
        file.write(printStr)
        file.close()
        messageBox(self, 21)
        system("notepad overallEmpReport.txt")


    def overallBookReport(self):
        records = self.bookCollection.find()
        printStr = str()
        totalBooks = int()
        totalIssued = int()
        avlBooksStr = "\n\nList of books available are as follows:"
        issuedBooksStr = "\n\nList of books issued are as follows:"

        for i in records:
            totalBooks += 1

            if i["noc"] > 0:
                avlBooksStr += "\n" + i["name"] + "\t" + i["code"]

        iRecords = self.issuedCollection.find()
        issued = []
        for i in iRecords:
            totalIssued += 2
            b1 = i["book1"]
            b2 = i["book2"]
            issued.append(b1)
            issued.append(b2)

        issued = set(issued)

        for i in issued:
            name = self.bookCollection.find_one({"code":i})["name"]
            issuedBooksStr += "\n" + name + "\t" + i

        printStr = "Total no. of books in the library: " + str(totalBooks) + "\n\n" + "Total no. of books issued: " + str(totalIssued) + avlBooksStr + issuedBooksStr
        file = open("overallBookReport.txt", "w")
        file.write(printStr)
        file.close()
        messageBox(self, 21)
        system("notepad overallBookReport.txt")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec_())
