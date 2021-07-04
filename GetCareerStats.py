#!/usr/bin/python3

import os
import funcs
import Parsers
from bs4 import BeautifulSoup

funcs = funcs.MyFuncs()
stat_parser = Parsers.StatsParser()


class CareerStats:
    def __init__(self):
        self.links_dir = "data/links/"
        self.players_dir = "data/players"
        self.link_files = self.get_link_files()

    def get_link_files(self):
        file_names = os.listdir(self.links_dir)
        for file in file_names:
            yield self.links_dir + file

    def get_stats(self):
        for file in self.link_files:
            cur_file = file.split("/")[-1][0]  # Returns the first letter of the current file.
            cur_dir = f"{self.players_dir}/{cur_file}"
            # Makes a directory with the name of the first letter of the link file
            # So that the players stats can be alphabetically organized.
            try:
                os.mkdir(cur_dir)
            except FileExistsError:
                pass
            print(f"Made dir {cur_dir}")
            # Gives all of the player names and links to stats
            player_info = funcs.read_file(file).split("\n")
            for player in player_info:
                if player:
                    name, link = player.split(", ")
                    print(f"Working on {name}")
                    player_file = f"{cur_dir}/{name}.txt"

                    try:
                        funcs.write_file(player_file, "")
                    except FileExistsError:
                        pass

                    stats_page = funcs.soup_request(link)
                    # PARSE STATS PAGE ##################################
                    meta = stat_parser.parse_meta(stats_page)
                    summary = stat_parser.get_summary(stats_page)

                    # Write info to file
                    for text in meta:
                        funcs.append_file(player_file, text)

                    funcs.append_file(player_file, "\n" + summary)

                    stat_parser.get_nhl_standard(stats_page)
                    #############################################
            break


stats = CareerStats()
stats.get_stats()
