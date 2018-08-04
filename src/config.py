import yaml
from os.path import expanduser

"""Fetches configuartion/key if exists else create a new"""

key_path=expanduser('config.yaml')

class ConfigReader(object):

    @classmethod
    def getKey(cls):
        """Fetches key"""

        with open(key_path,'r') as key_file:
            config=yaml.load(key_file)
            ConfigReader.__API_KEY=config['key']
        return ConfigReader.__API_KEY

    @classmethod
    def putKey(cls,key):
        """Creates a new config file"""

        with open(key_path,'w') as key_file:
            str='key : {}'.format(key)
            key_file.write(str)
