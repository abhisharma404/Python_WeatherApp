import requests

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
        print('-'*15)
        #print(self.URLGenerator_obj.get_url())
        return r
