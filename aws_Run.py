from classes.config_reader import ConfigReader
from classes.AWS_Connect import AWSConnector


class aws_runner(object):
    def __init__(self):
        self.aws_run = AWSConnector()


if __name__ == '__main__':
    print('-- AWS Run --')
    aws_runner = aws_runner()
    