import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()
handleForMedium = http.request("GET", "https://www.randomlists.com/random-names?qty=25")
source = handleForMedium.data

soup = BeautifulSoup(source, 'html.parser')

# print(soup.prettify())

for i in soup.find_all("div"):
    print(i.string)

file = open("DummyData/empNames.txt", "a")
