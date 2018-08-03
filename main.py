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

class WeatherApp(object):
    def __init__(self):
        self.URLGenerator_obj=None
        self.RequestGenerator_obj=None

    def main_func(self):
        key=input('Enter API Key ').strip()
        location=input('Enter location ').strip().lower()
        self.URLGenerator_obj=URLGenerator(user_api=key,location=location)
        self.RequestGenerator_obj=RequestGenerator(self.URLGenerator_obj)
        self.RequestGenerator_obj.request()


if __name__=='__main__':
    wa=WeatherApp()
    wa.main_func()
