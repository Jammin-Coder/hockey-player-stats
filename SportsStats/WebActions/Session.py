import requests
from .Soup import *


class Session:
    """
    This class is used to create a web sessions,
    make requests with the session, make soup requests.
    """
    def __init__(self):
        self.session = requests.Session()

    def get(self, url):
        response = self.session.get(url)
        return response.content

    def soup_request(self, url):
        # Makes BeautifulSoup with the contents of requested URL
        return soupify(self.get(url))
