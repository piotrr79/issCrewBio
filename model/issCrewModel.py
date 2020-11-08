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

    def getAstrosParserData(self):
        """ Get astronauts list from Wiki list by name """
        urls = self.parserUrls.split(',')
        response = {}
        for idx, url in enumerate(urls):
            parser = WikiParser(url)
            # @ToDo - extend iteration to accept results from different parsers (eg parsing by td not li)
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
        response = {} 
        for key, astroArray in astros.items():
            for astroItem in astroArray:
                # Join astro array to string
                astroString = ' '.join([str(elem) for elem in astroItem])           
                for item in crew:
                    # Extract surname (last part of string after last whitespace)
                    surname = (item.split(' ')[-1]).strip()                   
                    # Check if surname exist in string
                    regmatch = re.search(surname, astroString)
                    if regmatch != None:
                       crew[item] = astroItem
            # Push response (crew) from each iteration to final repsonse with key
            response[key] = crew
        return response

x = issCrew()
#astro = x.getAstrosParserData()
#crew = x.getCurrentCrew()
match = x.matchCrewWithAstros()
#print(astro)
#print(crew)
print(match)
