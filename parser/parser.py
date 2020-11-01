from urllib.request import urlopen
from bs4 import BeautifulSoup

class BaseParser:
    def __init__(self, url, element, class, needle, soupObject, attribute):
        self.url = url
        self.element = element
        self.class = class
        self.needle = needle
        self.soupObject = soupObject
        self.attribute = attribute

    def getContent(self.url):
        page = urlopen(self.url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        return html

    def getSoup():
        return BeautifulSoup(self.getContent(), "html.parser")

    '''def getElement(self.element):
        return self.getSoup().findAll(element, {"class": ""})'''

    def getElementByClass(self.element, self.class):
        return self.getSoup().findAll(element, {"class": class})

    def findInString(self.needle):
        return = str(self.getElement()).find(self.needle)

    def getText():
        return = self.getElement().get_text()

    def getAttribute(self.attribute):
        return = self.getElement().get(attribute)
