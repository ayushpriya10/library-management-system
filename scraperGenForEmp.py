import urllib3
from bs4 import BeautifulSoup
from random import randint

http = urllib3.PoolManager()
handleForMedium = http.request("GET", "https://www.randomlists.com/random-names?qty=25")
source = handleForMedium.data

soup = BeautifulSoup(source, 'html.parser')

# print(soup.prettify())

# for i in soup.find_all("div"):
#     print(i.string)

file = open("DummyData/empNames.txt", "r")
empDetailsFile = open("DummyData/empDetails.txt", "w")

# print(file.read())

names = [i for i in file.read().split("\n")]
print(len(names))

for name in names:
    print(name)

def codeGen(n):
    return "0"*(5-len(str(n))) + str(n)

def contactGen():
    return "990" + str(randint(1000000, 9999999))

# print(codeGen(3))

departments = ["Technical", "Administrative", "Finance", "Legal"]
detailString = str()

for i in range(1, 26):
    pin = codeGen(i)
    name = names[i-1]
    contact = contactGen()
    dept = departments[randint(0, 3)]

    detailString += pin + "," + name + "," + contact  + "," + dept + "\n"

print(detailString)

empDetailsFile.write(detailString)
empDetailsFile.close()
file.close()
