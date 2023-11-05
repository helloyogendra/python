from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")

def getLogFileName():
    return config["config"]["log_file"]


def getFileName():
    return config["config"]["file_name"]


