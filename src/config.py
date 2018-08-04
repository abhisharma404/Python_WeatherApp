import yaml
from os.path import expanduser

key_path=expanduser('config.yaml')

class ConfigReader(object):

    @classmethod
    def getKey(cls):
        with open(key_path,'r') as key_file:
            config=yaml.load(key_file)
            ConfigReader.__API_KEY=config['key']
        return ConfigReader.__API_KEY

    @classmethod
    def putKey(cls,key):

        with open('config.yaml','w') as key_file:
            str='key : {}'.format(key)
            key_file.write(str)
