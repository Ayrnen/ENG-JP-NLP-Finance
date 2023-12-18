from classes.Config_Reader import ConfigReader
from classes.Requester import Requester

import requests

class EDGAR_RESTClient(object):
    def __init__ (self, proxy=False, cloud=False):
        self.edgar_api_config = ConfigReader.get_edgar()
        self.headers = {'User-Agent': self.edgar_api_config['email']}
        self.cik_link = self.edgar_api_config['link']

    def cik_mapper(self):
        response = Requester.Request(
            self.cik_link,
            self.headers
        )

        print(response.json())