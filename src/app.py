import urllib
from generator import URLGenerator,RequestGenerator
from config import ConfigReader
import os
from os.path import expanduser

class DataFetcher(object):

    def __init__(self,RequestGenerator_obj,location):
        self.RequestGenerator_obj=RequestGenerator_obj
        self.location=location

    def getData(self):
        json_data=self.RequestGenerator_obj.request().json()
        print('Temperature of {} is {}'.format(self.location,json_data['main']['temp']))
        print('Humidity : {}'.format(json_data['main']['humidity']))

class WeatherApp(object):

    def __init__(self):
        self.URLGenerator_obj=None
        self.RequestGenerator_obj=None
        self.DataFetcher_obj=None
        self._key=None
        self.location=None

    def main_func(self):
        if os.path.isfile('config.yaml'):
            self._key=ConfigReader().getKey()
            self.location=input('Enter location ').strip().lower()

        else:
            self._key=input('Enter API Key ').strip()
            self.location=input('Enter location ').strip().lower()
            ConfigReader().putKey(self._key)
        self.location_encoded=urllib.parse.quote(self.location)
        self.URLGenerator_obj=URLGenerator(user_api=self._key,location=self.location_encoded)
        self.RequestGenerator_obj=RequestGenerator(self.URLGenerator_obj)
        self.DataFetcher_obj=DataFetcher(self.RequestGenerator_obj,location=self.location).getData()
