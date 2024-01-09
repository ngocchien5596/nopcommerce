import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations//config.ini")

class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getExpectLoginPageTitle():
        exp_login_title = config.get('common info', 'expected_login_title')
        return exp_login_title