import configparser

config = configparser.RawConfigParser()
# filePath = ".\\configuration\\config.ini"
filePath ="C:\\Users\\subha\\PycharmProjects\\iBridge360Aroha\\configuration\\config.ini"
config.read(filePath)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('url', 'baseURL')
        return url

    @staticmethod
    def getUserName():
        UserName = config.get('url', 'username')
        return UserName

    @staticmethod
    def getPassword():
        Password = config.get('url', 'password')
        return Password
