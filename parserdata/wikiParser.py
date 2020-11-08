from parserdata.parser import BaseParser

class WikiParser(BaseParser):
    """ Wikipedia lists parser """
    def __init__(self, url):
        super().__init__(url)

    # @ToDo - Add method getElementsByName() and get content of elelment by 1) attribute and by 2) text between elements
    
    # @ToDo - change method name to getSubElementsContnent with two options: 1) content by attribute (e.g. title, current way),
    # @ToDo - 2) get text between subelemnts (e.g. td, li, span)
    def getSubElementsByAttribute(self, element, classname, needle, subelement, attribute):
        """ Get html subelements of selected html element, get attribute content (title, img, alt, etc) """
        response = []
        items = self.getElementByClass(element, classname)
        for item in items:
            """ Check for search string / needle (element name, class, etc) in item """
            check = self.findInString(item, needle)
            if check != -1:
                """ Get subitems if needle found """
                subitems = self.getElementByName(item, subelement)
                subresponse = []
                # @ ToDo - add option to switch beetwen attributes and text iside sublements
                for subitem in subitems:
                    result = self.getAttribute(subitem, attribute)
                    subresponse.append(result)
                response.append(subresponse)

        return response

#x = WikiParser('https://en.wikipedia.org/wiki/List_of_astronauts_by_name')
#res = x.getSubElementsByAttribute('li', '', '<span class="flagicon">', 'a', 'title')
#print(res)
