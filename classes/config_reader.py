import configparser
import os

PATH = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = PATH + '/../.config.ini'
SECRET_FILE = PATH + '/../../secret/cautious.ini'

class ConfigReader(object):
    @staticmethod
    def get_jp_unicode(config_file=CONFIG_FILE):
        config = configparser.ConfigParser()
        config.read(config_file)
        
        return dict(
            hiragana_unicode = config.get('JP_Regex', 'hiragana'),
            katakana_unicode = config.get('JP_Regex', 'hiragana')
        )
    
    @staticmethod
    def get_aws_lvs(config_file=CONFIG_FILE, secret_file=SECRET_FILE):
        config = configparser.ConfigParser()
        config.read(config_file)
        secret = configparser.ConfigParser()
        secret.read(secret_file)

        return dict(
            access_key = secret.get('AWS_Lam_Store_Verbs', 'access_key'),
            secret_access_key = secret.get('AWS_Lam_Store_Verbs', 'secret_access_key'),
            region = config.get('AWS_Lam_Store_Verbs', 'region')
        )
    
    @staticmethod
    def get_edgar(config_file=CONFIG_FILE, secret_file=SECRET_FILE):
        config = configparser.ConfigParser()
        config.read(config_file)
        secret = configparser.ConfigParser()
        secret.read(secret_file)

        return dict(
            email = secret.get('EDGAR', 'email'),
            link = config.get('EDGAR', 'cik_link')
        )