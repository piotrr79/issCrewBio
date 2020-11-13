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
        # @ToDo - move to class EnvReader
        if os.environ.get('PARSER_URLS') is not None:   
            self.parserUrls = os.environ['PARSER_URLS']
            self.apiUrl = os.environ['API_URL']
            self.elementsDefinitions = os.environ['ELEMENTS_DEFINITIONS']
        else:
            self.parserUrls = config('PARSER_URLS')
            self.apiUrl = config('API_URL')
            self.elementsDefinitions = config('ELEMENTS_DEFINITIONS')
            
    def getArgs(self):
        """ Prepare list of elements to parse url against """
        response = []
        elements = self.elementsDefinitions.split('#')
        for element in elements:
            response.append(element.split(','))
        return response
    
    def getAstrosParserData(self):
        """ Get astronauts list from Wiki list by name """
        urls = self.parserUrls.split(',')
        response = {}
        for idx, url in enumerate(urls):
            parser = WikiParser(url)
            prseDef= self.getArgs()
            for args in prseDef:
                response[idx] = parser.getSubElementsContnent(*args)            
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
        # Astros contains data from several urls, itereate over all of them
        for key, astroArray in astros.items():
            # Itarate over astro data form single url (astroArray)
            for astroItem in astroArray:
                # Join astro array to string
                astroString = ' '.join([str(elem) for elem in astroItem])      
                # Check if astroArray item contains surnames from crew data
                for item in crew:
                    # Extract surname (last part of string after last whitespace)
                    surname = (item.split(' ')[-1]).strip()                   
                    # Check if surname exist in string
                    regmatch = re.search(surname, astroString)
                    if regmatch != None:
                        # Get old value from crew dictionary
                        oldVal = crew[item]                    
                        # If oldVal is empty set astroItem as oldVal (oldVal must be a type of list)
                        if not oldVal:
                            oldVal = astroItem
                        # Remove duplicates from new list (oldVal + astroItem) and set it as crew[item]
                        crew[item] = list(dict.fromkeys(oldVal + astroItem))
        return crew