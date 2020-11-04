from parserdata.parser import BaseParser

class WikiParser(BaseParser):
    """ Wikipedia lists parser """
    def __init__(self, url):
        super().__init__(url)

    def getSubElementsByAttribute(self, element, classname, needle, subelement, attribute):
        """ Get html subelements of selected html element, get attribute content (title, img, alt, etc) """
        response = []
        items = self.getElementByClass(element, classname)
        for item in items:
            check = self.findInString(item, needle)
            if check != -1:
                subitems = self.getElementByName(item, subelement)
                subresponse = []
                for subitem in subitems:
                    result = self.getAttribute(subitem, attribute)
                    subresponse.append(result)
                response.append(subresponse)

        return response

#x = WikiParser('https://en.wikipedia.org/wiki/List_of_astronauts_by_name')
#res = x.getSubElementsByAttribute('li', '', '<span class="flagicon">', 'a', 'title')
#print(res)
