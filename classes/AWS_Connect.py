from config_reader import ConfigReader
import os
import datetime as dt
import requests
import boto3
import botocore

class AWSConnector(object):
    def __init__ (self, proxy=False, cloud=False):
        self.aws_sdk = ConfigReader.get_aws_lvs()
        self.access_key = self.aws_sdk['access_key']
        self.secret_access_key = self.aws_sdk['secret_access_key']
        self.region = self.aws_sdk['region']
        self.mfa_serial = ''
        self.mfa_token = ''
        self.download_path = ''
        self.lambda_client = ''

        if cloud:
            ''
        else:
            ''
        
        if proxy:
            ''
        else:
            ''

    def get_temp_cred(self):
        sts = boto3.client('sts',
            aws_access_key_id = self.access_key
            aws_secret_access_key_id = self.secret_access_key
            config = botocore.config.Config(retries={'max_attempts':3, 'mode':'standard'})
        )
        
        response = sts.get_session_token(
            DurationSeconds = 9999,
            SerialNumber = self.mfa_serial,
            TokenCode = self.mfa_token
        )

        return response['Credentials']
    

    def s3_connection(self)
        credentials = self.get_temp_cred()

        s3_client = boto3.client(
            's3',
            aws_access_key_id = credentials['AccessKeyId']
            aws_secret_access_key = credentials['SecretAccessKey']
            aws_session_token = credentials['SessionToken']
            region_name = self.region
        )