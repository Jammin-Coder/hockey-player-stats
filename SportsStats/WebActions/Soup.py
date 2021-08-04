from bs4 import BeautifulSoup
from SportsStats.settings import HTML_PARSER

# Turns HTML into BeautifulSoup
def soupify(html) -> BeautifulSoup:
    return BeautifulSoup(str(html), HTML_PARSER)
