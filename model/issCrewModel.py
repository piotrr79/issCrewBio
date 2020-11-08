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
        self.parserUrls = config('PASER_URLS')
        self.apiUrl = config('API_URL')
        self.listDefinition = config('LIST_DEFINITION')
        self.tableDefinition = config('TABLE_DEFINITION')
        
    def getArgs(self):
        liElements = self.listDefinition.split(',')
        # @ToDo - improve tdElements definition
        tdElements = self.tableDefinition.split(',')
        return (liElements, tdElements)
    
    def getAstrosParserData(self):
        """ Get astronauts list from Wiki list by name """
        urls = self.parserUrls.split(',')
        response = {}
        for idx, url in enumerate(urls):
            parser = WikiParser(url)
            # parse every page in loop by elements definition
            prseDef= self.getArgs()
            for args in prseDef:
                subresponse = parser.getSubElementsByAttribute(*args)
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
