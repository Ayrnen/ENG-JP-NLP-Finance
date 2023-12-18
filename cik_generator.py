from classes.EDGAR_RESTClient import EDGAR_RESTClient

class cik_generator(object):
    def __init__(self):
        self.mapper = EDGAR_RESTClient()
        self.mapper.cik_mapper()


if __name__ == '__main__':
    obj = cik_generator()