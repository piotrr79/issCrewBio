import requests

class BaseApiReader():
    """ Iss api data reader """
    def __init__(self, url):
        self.url = url

    def getUrlData(self):
        """ Get data from api channel """
        try:
            return requests.get(self.url)
        except Exception as err:
            return str(err)