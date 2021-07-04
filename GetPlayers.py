#!/usr/bin/python3

import funcs

funcs = funcs.MyFuncs()


class GetPlayers:
    def __init__(self, url):
        self.player_num = 0
        self.chars = funcs.read_file("chars.txt")
        # self.current_char = 0
        self.data_dir = "./data"
        self.players_dir = f"{self.data_dir}/players"
        self.url = url
        self.html_parser = "lxml"

    # Returns all the "strong" tags in the players-div
    # The players within the strong tags are the ones currently playing

    def get_player_tags(self, char):
        current_url = f"{self.url}/players/{char}/"
        current_page = funcs.request(current_url)  # HTML of current page
        soup = funcs.soupify(current_page)  # Makes beautiful soup with current page
        players_div = soup.find("div", id="div_players")  # Extracts the player div
        souped_div = funcs.soupify(players_div)  # Makes soup with players_div

        # Finds all the p tags and returns them. The p tags hold the player name,
        # and link to the player's page.
        player_tags = funcs.soupify(souped_div.find_all("p", class_="nhl"))
        return player_tags.find_all("strong")

    # Returns a generator with the name and link in a dict
    def get_players(self, char):
        players = self.get_player_tags(char)
        for player in players:
            if not player.text == "None":
                player_link = self.url + player.a["href"]  # Returns the full url for the individual player's stats page
                player_name = player.text  # Player name/career duration.
                yield {"name": player_name, "site_path": player_link}
        # Tells program to move the next char
        # self.current_char += 1

    def run(self):
        for char in self.chars:
            print(f">> Working on {char}")
            players = self.get_players(char)
            link_file = f"{self.data_dir}/links/{char}.txt"
            funcs.write_file(link_file, "")
            for player in players:
                self.player_num += 1
                player_name = player["name"]
                player_page = player["site_path"]
                funcs.append_file(link_file, player_name + ", " + player_page)
        print(f"Found {self.player_num} players total.")
