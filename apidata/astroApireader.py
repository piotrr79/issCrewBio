from apidata.apireader import BaseApiReader

class issDataReader(BaseApiReader):
    """ Iss api data reader """
    def __init__(self, url):
        super().__init__(url)

    def getAstroData(self):
        """ Parse data from api channel """
        astros = self.getUrlData()
        if astros.status_code == 200:
            astros = astros.json()
        else:
            raise Exception('Api did not return valid response')
        response = []
        print(astros)
        if 'people' in astros:
            #print(astros.get('people'))
            for astro in astros.get('people'):
                response.append(astro.get('name')) 
        return response
