# For projects sometimes we need to read config files
# These config files can have various static data, like port, server-ip, user-name, log-information
# we can create a config.ini file and here we can keep our static information required by project

# in this example we are reading config.ini file and storing it in a dictionary, later we can use that information in our project

# config.ini file

import os
from pathlib import Path
from configparser import ConfigParser





def get_config():
    try:
        config = ConfigParser()
        config_file_path_1 = os.path.join(os.path.dirname(__file__), 'config.ini')
        config_file_path_2 = Path(__file__).parent / 'config.ini'
        config.read(config_file_path_2)
        
        return config
    except Exception as ex:
        print(ex.__traceback__.tb_lineno)
        print("error")
        return None

    


def get_port():
    config = get_config()

    if config is None:
        raise Exception("Unable to read or load the config")
    else:
        return config['server']['server_port']
    

def get_server_name():
    config = get_config()

    if config is None:
        raise Exception("Unable to read or load the config")
    else:
        return config['server']['server_name']
    

def get_db_name():
    config = get_config()

    if config is None:
        raise Exception("Unable to read or load the config")
    else:
        return config['server']['server_db']
    



port = get_port()
print("port from config file is'{0}'".format(port))

server_name = get_server_name()
print("server_name from config file is'{0}'".format(server_name))

db_name = get_db_name()
print("db_name from config file is '{0}'".format(db_name))