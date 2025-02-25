
import requests
from requests.auth import HTTPDigestAuth
import json

class Valuator_Processor:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Valuator_Processor, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.scryfall_home = "https://api.scryfall.com/"
        self.card_name = ""
        self.card_url = ""
        self.data = ""

    def check_url(self):
        my_response = requests.get(self.scryfall_home + self.card_url)
        if (my_response.ok):
            return json.loads(my_response.content)
        else:
            raise TypeError("error " + my_response.status_code + " " + my_response.text)

    def process_url(self, url):
          self.card_url = url
          return self.check_url()



