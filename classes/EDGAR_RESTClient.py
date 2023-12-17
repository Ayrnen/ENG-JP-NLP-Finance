from classes.config_reader import ConfigReader

import requests

class EDGAR_RESTClient(object):
    def __init__ (self, proxy=False, cloud=False):
        self.edgar_api_config = ConfigReader.get_edgar()
        self.headers = {'User-Agent': self.edgar_api_config['email']}
        self.cik_link = self.edgar_api_config['link']

    def grab_cik(self):
        response = requests.get(
            self.cik_link,
            headers = self.headers
        )

        print(response.status_code)