from urllib.request import urlopen
from bs4 import BeautifulSoup

class BaseParser:
    """ Html parses common methods """
    def __init__(self, url):
        self.url = url

    def getContent(self, url):
        """ Get content of html page from url """
        page = urlopen(url)
        html_bytes = page.read()
        return html_bytes.decode("utf-8")

    def getSoup(self):
        """ Parse html with BeautifulSoup parser """
        return BeautifulSoup(self.getContent(self.url), "html.parser")

    def getElementByClass(self, element, classname):
        """ Get html element by name and class """
        return self.getSoup().findAll(element, {"class": classname})
    
    def getElementByName(self, soup, htmlelement):
        """ Get html element by name and class from provided html parsed by BeautifulSoup """
        return soup.findAll(htmlelement, {"class": ""})
    
    def findInString(self, element, needle):
        """ Find needle in provided element (BeautifulSoup onbject) """
        return str(element).find(needle)

    def getText(self, element):
        """ Get text from provided elemenet """
        return element.get_text()

    def getAttribute(self, element, attribute):
        """ Get content of provided attribute (title, alt) for given elelement """
        return element.get(attribute)