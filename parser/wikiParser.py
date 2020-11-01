from parser import BaseParser

class WikiParser(BaseParser):
    def __init__(self, url):
        super().__init__(url)

    def getLinks(self, element, classname, needle, subelement, attribute):
        response = []
        elements = self.getElementByClass(element, classname)
        for idx, element in enumerate(elements):
            check = self.findInString(needle)
            if check != -1:
                subelements = self.getElement(element)
                subresponse = []
                for subelement in subelements:
                    result = self.getAttribute(attribute)
                    subresponse.append(result)
            response[idx].append(subresponse)

        return response

x = WikiParser('https://en.wikipedia.org/wiki/List_of_astronauts_by_name')
res = x.getLinks('li', '', '<span class="flagicon">', 'a', 'title')
print(res)
