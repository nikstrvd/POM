import configparser

config = configparser.RawConfigParser()
config.read('Configurations/config.ini')


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('Common info', 'BaseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('Common info', 'Username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Common info', 'Password')
        return password
