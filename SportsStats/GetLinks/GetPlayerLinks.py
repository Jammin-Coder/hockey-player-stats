from SportsStats.Parsers.Urls import *
from SportsStats.FileSystem import file_system_utils as fs


class GetPlayerLinks:
    """
    This class gets all of the URLs to the players' stats pages.
    """
    def __init__(self, base_url, mode=None):
        self.base_url = base_url  # Normal URL of the website
        self.session = Session()  # New web session.
        # Uses the GetUrls class and gets th alphabetized page indices.
        self.urls = GetUrls(self.base_url)
        self.page_indices = self.urls.get_page_indices()

        if mode == "pro":
            self.mode = mode
        else:
            self.mode = "all"

    def get_players_on_page(self, url) -> list:
        """
        Returns a list that contains dictionaries which have
        "name" and "url" keys.
        :param url:
        :return {"name": player_name, "url": player_url}:
        """
        # List of dictionaries with player name and player url
        # {"name": player_name, "url": player_url}
        players_list = []

        page_contents = self.session.soup_request(url)
        # Gets the <div> that contains all of the players on this page.
        players_div = soupify(page_contents.find("div", {"id": DIV_PLAYERS}))

        # Chooses weather to get all players, or pro players only.
        if self.mode == "pro":
            players = players_div.find_all("p", class_="nhl")
        else:
            players = players_div.find_all("p")

        current_char = get_last_url_char(url)
        print(f"Working on {current_char}")

        for player in players:
            player_name = parse_name(player.text).lower()
            player_link = f'{current_char}/{player.a["href"].split("/")[-1]}'
            players_list.append({"name": player_name, "url": player_link})
        return players_list

    def get_all_player_urls(self) -> None:
        """
        This function gets all of the links to each players' stats pages
        :return:
        """
        data = dict()
        data["base_link"] = join_urls(self.base_url, PLAYERS_PATH)
        for url in self.page_indices:
            page_contents = self.session.soup_request(url)
            # Gets the <div> that contains all of the players' urls
            players_div = soupify(page_contents.find("div", {"id": DIV_PLAYERS}))

            if self.mode == "pro":
                players = players_div.find_all("p", class_="nhl")
            else:
                players = players_div.find_all("p")

            current_char = get_last_url_char(url)
            print(f"Working on {current_char}")
            # Creates a character key in the data dictionary whose value is another dictionary.
            data[current_char] = dict()

            # Loops over all of the players and extracts their name and the url to their stats page.
            for player in players:
                player_name = parse_name(player.text).lower()
                abbrev_player_name = player.a["href"].split("/")[-1]  # Gets the abbreviated player name from the URL
                player_url = f'{current_char}/{abbrev_player_name}'
                # This is where you decide what to do with the data

                # Adds the key-value data pair for this player name and url to the data dictionary
                data[current_char].update({player_name: player_url})

        # Do stuff with the acquired data:
        fs.del_file_content(LINKS_JSON_FILE)
        fs.write_json(LINKS_JSON_FILE, data)
