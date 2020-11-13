from parserdata.parser import BaseParser

class WikiParser(BaseParser):
    """ Wikipedia lists parser """
    def __init__(self, url):
        super().__init__(url)

    def getSubElementsContnent(self, element, classname, needle, subelement, attribute):
        """ Get html subelements of selected html element, get attribute content (title, img, alt, etc) or text inside element """
        response = []
        items = self.getElementByClass(element, classname)
        for item in items:
            """ Check for search string / needle (element name, class, etc) in item """
            check = self.findInString(item, needle)
            subresponse = []
            if check != -1:
                """ Get subitems if needle found """
                subitems = self.getElementByName(item, subelement)                
                result = []
                """ If attribute is set get atribute content, if not get text between elements """
                for subitem in subitems:
                    # Get attribute value, if no attribute get subelements text
                    if attribute:
                        result.append(self.getAttribute(subitem, attribute))
                    else:
                        result.append(self.getText(subitem))
                subresponse.append(result)
            response.append(subresponse)
        return response
