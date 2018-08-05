import requests

class URLGenerator(object):
    """This will generate the URL for fetching the API data"""

    def __init__(self,user_api,location):
        self.location=location
        self.user_api=user_api
        self.BASE_URL='https://api.openweathermap.org/data/2.5/weather?q='+self.location+'&APPID='+self.user_api

    @property
    def url(self):
        """Returns the created URL"""

        return self.BASE_URL

class RequestGenerator(object):

    def __init__(self,URLGenerator_obj):
        self.URLGenerator_obj=URLGenerator_obj

    @property
    def request(self):
        """Connects to the URL"""

        r=requests.get(self.URLGenerator_obj.url)
        print('-'*15)
        return r
