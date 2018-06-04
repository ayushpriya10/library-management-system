from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()
handleForMedium = http.request("GET", "https://medium.com/@sampadasharma/list-of-best-mechanical-engineering-books-for-student-5e78e04ff264")
source = handleForMedium.data

soup = BeautifulSoup(source, 'html.parser')

# print(soup.prettify())
count = 0
listOfBooks = list()

for i in soup.find_all("li"):
    try:
        if i["class"] == ["graf", "graf--li", "graf-after--li"]:
            if "by" in i.string:
                name, author = i.string.split("by")
                # print(name + ":::::" + author)
                if [name, author] not in listOfBooks:
                    listOfBooks.append([name, author])
            else:
                print(i.string)
            count += 1
    except:
        pass

print(count)

file = open("DummyData/booksAndAuthor.txt", "a")

for i in listOfBooks:
    try:
        # print(i)
        file.write(str(i[0]).strip() + "," + str(i[1]).strip() + "\n")
    except:
        print(i)
file.close()

print(len(listOfBooks))
