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
        self.firstParserUrl = config('FIRST_URL')
        self.secondParserUrl = config('SECOND_URL')
        self.thirdParserUrl = config('THIRD_URL')
        self.parserUrls = config('PASER_URLS')
        self.element = config('ELEMENT')
        self.classname = config('CLASS_NAME')
        self.needle = config('NEEDLE')
        self.subelement = config('SUBELEMENT')
        self.attribute = config('ATTRIBUTE')
        self.apiUrl = config('API_URL')
    
    def getAllAstrosByName(self):
        """ Get astronauts list from Wiki list by name """
        parser = WikiParser(self.firstParserUrl )
        return parser.getSubElementsByAttribute(self.element, self.classname, self.needle, self.subelement, self.attribute)

    def getAllAstrosTravelers(self):
        """ Get travelers list from Wiki travelers by name """
        parser = WikiParser(self.secondParserUrl)
        return parser.getSubElementsByAttribute(self.element, self.classname, self.needle, self.subelement, self.attribute)
    
    # Set up different parsing elements
    # @ToDo - test parser with td elements on that 
    def getAllAstrosByFirstFlight(self):
        """ Get astronauts list from Wiki by first flight """
        parser = WikiParser(self.thirdParserUrl)
        return parser.getSubElementsByAttribute(self.element, self.classname, self.needle, self.subelement, self.attribute)

    def getAstrosParserData(self):
        """ Get astronauts list from Wiki list by name """
        urls = self.parserUrls.split(',')
        response = {}
        for idx, url in enumerate(urls):
            parser = WikiParser(url)
            subresponse = parser.getSubElementsByAttribute(self.element, self.classname, self.needle, self.subelement, self.attribute)
            response[idx] = subresponse
        return response
    
    def getCurrentCrew(self):
        """ Get ISS crew """
        crew = issDataReader(self.apiUrl)
        # Transform list to dictionary
        return dict.fromkeys(crew.getAstroData(), '') 
        
    def matchCrewWithAstros(self):
        """ Match ISS crew members with country and otjer available data """
        astros = self.getAstrosParserData()      
        crew = self.getCurrentCrew() 
        for key, astroArray in astros.items():
            # Join astro array to string
            for astroItem in astroArray:
                """ Create strinf from element """
                astroString = ' '.join([str(elem) for elem in astroItem]) 
                for item in crew:
                    # Extract surname (last part of string after last whitespace)
                    surname = (item.split(' ')[-1]).strip()
                    # Check if surname exist in string
                    regmatch = re.search(surname, astroString)
                    if regmatch != None:
                        crew[item] = {key: astroItem}
                        '''if crew[item] is None:
                            crew[item] = astroItem
                        else:
                            oldVal = crew[item]
                            print(oldVal)
                            print(astroItem)
                            #crew[item].append(astroItem)
                            crew[item] = oldVal + astroItem'''
            return crew

x = issCrew()
#astro1 = x.getAllAstrosByName()
#astro2 = x.getAllAstrosTravelers()
#astro3 = x.getAllAstrosByFirstFlight()
#astro4 = x.getAstrosParserData()
#crew = x.getCurrentCrew()
match = x.matchCrewWithAstros()
#print(astro1)
#print(astro2)
#print(astro3)
#print(astro4)
#print(crew)
print(match)
