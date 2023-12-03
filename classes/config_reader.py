import configparser
import os

PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = PATH + '/../.config.ini'

class ConfigReader(object):
    @staticmethod
    def get_jp_unicode(filename=CONFIG_FILE):
        config = configparser.ConfigParser()
        config.read(filename)
        return dict(
            hiragana_unicode = config.get('JP_Regex': 'hiragana'),
            katakana_unicode = config.get('JP_Regex': 'hiragana')
        )
    
    @staticmethod
    def get_aws_lvs(filename=CONFIG_FILE):
        config = configparser.ConfigParser()
        config.read(filename)
        return dict(
            access_key = config.get('AWS_Lam_Store_Verbs': 'access_key'),
            secret_access_key = config.get('AWS_Lam_Store_Verbs': 'secret_access_key'),
            region = config.get('AWS_Lam_Store_Verbs': 'region')
        )