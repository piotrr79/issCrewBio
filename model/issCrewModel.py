import sys
import os
# Tell syspath where to import modules from other folders in root direcotry
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from decouple import config
import re
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
        # Transform list to dictionary
        return dict.fromkeys(crew.getAstroData(), '') 
        
    def matchCrewWithAstros(self):
        """ Match ISS crew members with country """
        astros = self.getAllAstros()
        crew = self.getCurrentCrew()
        # Switch list to dictionary
        for astro in astros:
            # Join astro array to string
            astroString = ' '.join([str(elem) for elem in astro]) 
            for item in crew:
                # Extract surname (last part of string after last whitespace)
                surname = (item.split(' ')[-1]).strip()
                # Check if surname exist in string
                regmatch = re.search(surname, astroString)
                if regmatch != None:
                    crew[item] = astro
        return crew

x = issCrew()
#astro = x.getAllAstros()
#crew = x.getCurrentCrew()
match = x.matchCrewWithAstros()
#print(astro)
#print(crew)
print(match)
