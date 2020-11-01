from urllib.request import urlopen
from bs4 import BeautifulSoup

class BaseParser:
    def __init__(self, url):
        self.url = url

    def getContent(url):
        page = urlopen(url)
        html_bytes = page.read()
        return html_bytes.decode("utf-8")

    def getSoup(self):
        return BeautifulSoup(self.getContent(), "html.parser")

    def getElement(element):
        return self.getSoup().findAll(element, {"class": ""})

    def getElementByClass(self, element, classname):
        return self.getSoup().findAll(element, {"class": classname})

    def findInString(element, needle):
        return str(element).find(needle)

    def getText(element):
        return element.get_text()

    def getAttribute(element, attribute):
        return element.get(attribute)
