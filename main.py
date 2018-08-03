#Weather App Initial Stage
import requests
import sys

class URLGenerator(object):


    def __init__(self,user_api,location):
        self.location=location
        self.BASE_URL='https://api.openweathermap.org/data/2.5/weather?q='+self.location
        self.API_KEY_URL='&APPID='
        self.API_KEY=' '
        self.API_KEY_URL+=user_api
        self.BASE_URL+=self.API_KEY_URL

    def get_url(self):
        return self.BASE_URL

class RequestGenerator(object):
    def __init__(self,URLGenerator_obj):
        self.URLGenerator_obj=URLGenerator_obj

    def request(self):
        r=requests.get(self.URLGenerator_obj.get_url())
        print(self.URLGenerator_obj.get_url())
        if r.status_code==200:
            print('Connected')
        else:
            print('Error')
        return r

class WeatherApp(object):
    def __init__(self):
        self.URLGenerator_obj=None
        self.RequestGenerator_obj=None
        self.DataFetcher_obj=None
        self.key=None
        self.location=None

    def main_func(self):
        self.key=input('Enter API Key ').strip()
        self.location=input('Enter location ').strip().lower()
        self.URLGenerator_obj=URLGenerator(user_api=self.key,location=self.location)
        self.RequestGenerator_obj=RequestGenerator(self.URLGenerator_obj)
        self.RequestGenerator_obj.request()
        self.DataFetcher_obj=DataFetcher(self.RequestGenerator_obj,location=self.location)
        self.DataFetcher_obj.getData()

class DataFetcher(object):

    def __init__(self,RequestGenerator_obj,location):
        self.RequestGenerator_obj=RequestGenerator_obj
        self.location=location

    def getData(self):
        json_data=self.RequestGenerator_obj.request().json()
        print('Temperature of {} is {}'.format(self.location,json_data['main']['temp']))

if __name__=='__main__':
    wa=WeatherApp()
    wa.main_func()
