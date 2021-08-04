from SportsStats.WebActions.web_actions import *
from SportsStats.settings import *
from .parser_utils import *


class GetUrls:
    """
    This class returns a list that contains links to the alphabetically organized
    player pages.
    I.E the first page will be https://www.hockey-reference.com/a,
    this is a link to the page that contains all of the players who's name start with "a".
    The next page will be https://www.hockey-reference.com/a,
    this link goes to the page that contains all of the players who's name starts with "b".
    It does this all the way to "z".
    """
    def __init__(self, base_url):
        self.base_url = base_url  # Normal URL of the website
        self.players_url = join_urls(self.base_url, "/players/")  # URL to the players index page
        self.session = Session()  # Creates new web session
        # Gets the player page and turns it into BeautifulSoup
        self.players_page = soupify(self.session.get(self.players_url))

    def get_page_indices(self) -> list:
        """
        Returns a list of URLs for all of the player groups.
        ["{self.base_url}/players/a", "{self.base_url}/players/b", "{self.base_url}/players/c",
            "{self.base_url}/players/etc.."]
        :return:
        """
        # Gets the <ul> that contains the alphabetized index
        page_index = self.players_page.find("ul", class_=PAGE_INDEX)
        # Makes BeautifulSoup with the page index <ul>s
        page_index = soupify(page_index)
        # Gets the <li>s that contain the <a> tags and page links
        li_tags = page_index.find_all("li")

        # TODO: Make these 2 comprehensions neater
        # Gets all of the <a> tags containing the links to player pages
        a_tags = soupify([li.a for li in li_tags]).find_all("a")
        # Gets the links from a_tags and joins them with the base URL
        player_page_links = [join_urls(self.base_url, (a["href"])) for a in a_tags]
        return player_page_links
