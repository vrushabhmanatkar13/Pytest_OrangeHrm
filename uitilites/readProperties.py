import configparser


def getConfig():
    config = configparser.RawConfigParser()
    config.read("./Configiuration/config.ini")
    return config
