from urllib.request import urlopen
from bs4 import BeautifulSoup
from parser import BaseParser

class WikiParser(Parser):
    def __init__(self, url, element, class, needle, soupObject, attribute):
        super().__init__(url, element, class, needle, soupObject, attribute)

    def getLinks():


    mylis = soup.findAll("li", {"class": ""})
    for myli in mylis:
        astr = str(myli).find('<span class="flagicon">')
        if astr != -1:
            links = myli.findAll("a", {"class": ""})
            for link in links:
                title = link.get('title')
                print(title)
