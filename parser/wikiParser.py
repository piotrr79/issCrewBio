from parser import BaseParser

class WikiParser(BaseParser):
    def __init__(self, url):
        super().__init__(url)

    def getLinks(self, element, classname, needle, subelement, attribute):
        response = []
        items = self.getElementByClass(element, classname)
        for idx, item in enumerate(items):
            check = self.findInString(item, needle)
            if check != -1:
                subitems = self.getElementByName(item, subelement)
                subresponse = []
                for idx, subitem in enumerate(subitems):
                    result = self.getAttribute(subitem, attribute)
                    subresponse.append(result)
                response.append(subresponse)

        return response

x = WikiParser('https://en.wikipedia.org/wiki/List_of_astronauts_by_name')
res = x.getLinks('li', '', '<span class="flagicon">', 'a', 'title')
print(res)
