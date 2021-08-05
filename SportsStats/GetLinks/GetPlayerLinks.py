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

    def get_players_on_page(self, url) -> None:
        """
        Returns a list that contains dictionaries which have
        "name" and "url" keys.
        :param url:
        :return {"name": player_name, "url": player_url}:
        """

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

        # Makes text file to store all urls of the current character
        link_file = f"{LINKS_DIR}/{current_char}.txt"
        fs.write(link_file, "")

        for player in players:
            player_name = parse_name(player.text).lower()

            # The player url in the format: "/players/char/player_name"
            player_url = player.a["href"]
            data_line = f"{player_name}: {player_url}\n"
            fs.append(link_file, data_line)

    def get_all_player_urls(self) -> None:
        fs.init_data_dir()  # Initializes the base data directories.
        for url in self.page_indices:
            self.get_players_on_page(url)
