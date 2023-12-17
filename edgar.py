from classes.config_reader import ConfigReader
from classes.EDGAR_RESTClient import EDGAR_RESTClient

class EDGAR_Collection(object):
    def __init__(self):
        self.edgar_connect = EDGAR_RESTClient()
    
    def run_cik(self):
        self.edgar_connect.grab_cik()




if __name__ == '__main__':
    # format class start method
    
    obj = EDGAR_Collection()
    obj.run_cik()




    # format class end method