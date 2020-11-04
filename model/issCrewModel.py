import sys
import os
from decouple import config
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from apidata.astroApireader import issDataReader
from parserdata.wikiParser import WikiParser

class issCrew():
    """ Iss crew members by country """
    def __init__(self):
        #pass
        self.parserUrl = config('URL')
        self.element = config('ELEMENT')
        self.classname = config('CLASS_NAME')
        self.needle = config('NEEDLE')
        self.subelement = config('SUBELEMENT')
        self.attribute = config('ATTRIBUTE')
        self.apiUrl = config('API_URL')
    
    def getAllAstros(self):
        """ Get astronauts list by name from Wiki """
        parser = WikiParser(self.parserUrl)
        return parser.getSubElementsByAttribute(self.element, self.classname, self.needle, self.subelement, self.attribute)

    def getCurrentCrew(self):
        """ Get ISS crew """
        crew = issDataReader(self.apiUrl)
        return crew.getAstroData()
        
    def matchCrewWithAstros(self):
        """ Match ISS crew members with country """
        astros = self.getAllAstros()
        crew = self.getCurrentCrew()
        astrodetail = []
        for astro in astros:
            for item in crew:
                # split item, reverse array and get first element to extract surname
                #print(item)
                array = item.split()
                array.sort(reverse=False)
                print(array)
                for subitem in array:
                    #print(subitem)
                    if subitem in astro:
                        astrodetail.append(astro) 
                        astrodetail.append(item)
        return astrodetail

x = issCrew()
#astro = x.getAllAstros()
crew = x.getCurrentCrew()
match = x.matchCrewWithAstros()
#print(astro)
print(crew)
print(match)
