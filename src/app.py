import urllib
from generator import URLGenerator,RequestGenerator
from config import ConfigReader
import os
from os.path import expanduser
from utils.csv_writer import *

class DataFetcher(object):
    """Fetches the data from the generated URL"""

    def __init__(self,RequestGenerator_obj,location):
        self.RequestGenerator_obj=RequestGenerator_obj
        self.location=location
        self.json_data=''

    def getData(self):
        try:
            self.json_data=self.RequestGenerator_obj.request().json()
        except:
            print('There is a problem in your connection.')
        if self.json_data:
            try:
                print('Temperature of %s is %i C'%(self.location,self.json_data['main']['temp']-273.15))
                print('Humidity : {}'.format(self.json_data['main']['humidity']))
                print('Pressure : {}'.format(self.json_data['main']['pressure']))
                print('Wind Speed : {}'.format(self.json_data['wind']['speed']))
                print('Visibility : {}'.format(self.json_data['visibility']))
            except KeyError:
                pass
            finally:
                print('-'*15)

    def exportData(self):
        try:
            self.CSVWriter_obj=CSVWriter()
            self.CSVWriter_obj.write_data(Location=self.location,Temperature=self.json_data['main']['temp']-273.15,Humidity=self.json_data['main']['humidity'])
            print('Data transferred to CSV, path is -> '+filepath)
        except:
            print('Could not save the data into CSV format.Please try again.')

class WeatherApp(object):

    def __init__(self):
        self.URLGenerator_obj=None
        self.RequestGenerator_obj=None
        self.DataFetcher_obj=None
        self._key=None
        self.location=None

    def keyConfig(self):
        self._key=input('Enter API Key ').strip()
        ConfigReader().putKey(self._key)

    def main_func(self):
        if os.path.isfile('config.yaml'):
            self._key=ConfigReader().getKey()
            if not self._key:
                self.keyConfig()
            self.location=input('Enter location ').strip().lower()
        else:
            self._key=input('Enter API Key ').strip()
            self.keyConfig()
        self.location_encoded=urllib.parse.quote(self.location)
        self.URLGenerator_obj=URLGenerator(user_api=self._key,location=self.location_encoded)
        self.RequestGenerator_obj=RequestGenerator(self.URLGenerator_obj)
        self.DataFetcher_obj=DataFetcher(self.RequestGenerator_obj,location=self.location)
        self.DataFetcher_obj.getData()

        print('Print data to a CSV file?')
        if input()=='Y':
            self.DataFetcher_obj.exportData()
