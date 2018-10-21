from random import randint
from pymongo import MongoClient

def printList(l):
    for i in l:
        print(i)

empDetailFile = open("DummyData/empDetails.txt")
bookDetailFile = open("DummyData/bookDetails.txt")

empDetails = empDetailFile.read().split("\n")
empDetails = empDetails[:-1]
# printList(empDetails)

bookDetails = bookDetailFile.read().split("\n")
bookDetails = bookDetails[:-1]
# printList(bookDetails)

db = MongoClient("mongodb://localhost:27017/")["lms"]

bookCollection = db["books"]
empCollection = db["emp"]

for i in bookDetails:
    name, author, publisher, cost, code = i.split(",")
    # print(name, author, publisher, cost, code)

    bookCollection.insert({"name":name, "code":code, "author":author, "cost":cost, "publisher":publisher, "issueID":"", "noc":randint(1,2)})

for i in empDetails:
    code, name, contact, dept = i.split(",")
    # print(code, name, contact, dept)

    empCollection.insert({"PIN":code, "name":name, "contact":contact, "dept":dept, "issueID":""})
    
    
    .
