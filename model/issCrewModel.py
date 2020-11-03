import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from apidata.astroApireader import issDataReader
from parser.wikiParser import WikiParser

class issCrew():
    """ Iss crew members by country """
    def __init__(self):
        pass
    
    def getAllAstros(self, url, element, classname, needle, subelement, attribute):
        """ Get astronauts list by name from Wiki """
        parser = WikiParser(url)
        return parser.getSubElementsByAttribute(element, classname, needle, subelement, attribute)

    def getCurrentCrew(self, url):
        """ Get ISS crew """
        crew = issDataReader(url)
        return crew.getAstroData()


x = issCrew()
astro = x.getAllAstros('https://en.wikipedia.org/wiki/List_of_astronauts_by_name', 'li', '', '<span class="flagicon">', 'a', 'title')
crew = x.getCurrentCrew('http://api.open-notify.org/astros.json')
print(astro)
print(crew)
