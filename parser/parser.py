from urllib.request import urlopen
from bs4 import BeautifulSoup

class BaseParser:
    def __init__(self, url):
        self.url = url

    def getContent(self, url):
        page = urlopen(url)
        html_bytes = page.read()
        return html_bytes.decode("utf-8")

    def getSoup(self):
        return BeautifulSoup(self.getContent(self.url), "html.parser")

    def getElement(self, htmlelement):
        return self.getSoup().findAll(htmlelement, {"class": ""})

    def getElementByClass(self, element, classname):
        return self.getSoup().findAll(element, {"class": classname})

    def getElementByName(self, soup, htmlelement):
        return soup.findAll(htmlelement, {"class": ""})

    def findInString(self, element, needle):
        return str(element).find(needle)

    def getText(self, element):
        return element.get_text()

    def getAttribute(self, element, attribute):
        return element.get(attribute)
