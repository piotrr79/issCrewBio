from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_astronauts_by_name"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

soup = BeautifulSoup(html, "html.parser")

mylis = soup.findAll("li", {"class": ""})
for myli in mylis:
    astr = str(myli).find('<span class="flagicon">')
    if astr != -1:
        links = myli.findAll("a", {"class": ""})
        for link in links:
            title = link.get('title')
            print(title)

class BaseParser:
    def __init__(self):

    def getContent(url):
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        return html

    def getSoup():
        return BeautifulSoup(self.getContent(), "html.parser")

    def getElement(element):
        return self.getSoup().findAll(element, {"class": ""})

    def getElementByClass(element, class):
        return self.getSoup().findAll(element, {"class": class})

    def findInString(needle):
        return = str(self.getElement()).find(needle)

    getText()
astronauts = myli.get_text()
