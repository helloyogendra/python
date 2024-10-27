class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
s1 = Singleton()
s2 = Singleton()

print(s1 == s2)  # Output: True, both are the same instance




#
# Singleton Logger Class

import logging

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            logging.basicConfig(level=logging.INFO)
            cls._logger = logging.getLogger(__name__)
        return cls._instance

    def info(self, message):
        self._logger.info(message)

    def error(self, message):
        self._logger.error(message)

# Usage
logger = Logger()
logger.info("This is an info message.")





# Singleton Config Reader Class

import json

class ConfigReader:
    _instance = None

    def __new__(cls, config_file='config.json'):
        if cls._instance is None:
            cls._instance = super(ConfigReader, cls).__new__(cls)
            with open(config_file, 'r') as f:
                cls._config = json.load(f)
        return cls._instance

    def get(self, key):
        return self._config.get(key)

# Usage
config_reader = ConfigReader()
db_host = config_reader.get("database_host")
