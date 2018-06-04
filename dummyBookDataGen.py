booksAndAuthorsFile = open("DummyData/booksAndAuthor.txt")
detailsFile = open("DummyData/bookDetails.txt", "w")
publishersFile = open("DummyData/publishers.txt")

from random import randint
count = 0
booksAndAuthors = booksAndAuthorsFile.read().split("\n")
for i in booksAndAuthors[:len(booksAndAuthors)-1]:
    print(i)
    count += 1
print(count)

count = 0
publishers = publishersFile.read().split("\n")
prefix = ["G", "M", "T", "F"]
for i in publishers:
    print(i)
    count += 1
print(count)

detailString = str()

for i in range(4):
    bookCount = 0
    publisherIndex = 0

    for j in range(5):
        name, author = booksAndAuthors[i*4 + j].split(",")
        # print(booksAndAuthors[i*4 + j].split(","))
        cost = randint(1000, 5000)
        publisher = publishers[(i*4+j)%10]
        code = prefix[i] + "00" + str(j)

        detailString += name + "," + author + "," + publisher + "," + str(cost) + "," + code + "\n"

print(detailString)

count = 0
for record in detailString.split("\n")[:len(detailString.split("\n"))-1]:
    i,j,k,l,m = record.split(",")
    # print(record.split(","))
    print(i,j,k,l,m)
    count += 1

print(count)

detailsFile.write(detailString)

detailsFile.close()
booksAndAuthorsFile.close()
publishersFile.close()
