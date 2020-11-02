from parser import BaseParser

class WikiListParser(BaseParser):
    def __init__(self, url):
        super().__init__(url)

    def getLinks(self):
        response = []
        elements = self.getElementByClass('li', '')
        for idx, item in enumerate(elements):
            check = self.findInString(item, '<span class="flagicon">')
            if check != -1:
                subelements = self.getElementByName(item, 'a')
                print(subelements)
                subresponse = []
                for idx, subelement in enumerate(subelements):
                    result = self.getAttribute(subelement, 'title')
                    subresponse.append(result)
                response.append(subresponse)

        return response

x = WikiListParser('https://en.wikipedia.org/wiki/List_of_astronauts_by_name')
res = x.getLinks()
print(res)
