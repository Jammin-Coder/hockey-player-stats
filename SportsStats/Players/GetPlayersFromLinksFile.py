from .GetPlayer import *
from SportsStats.FileSystem import file_system_utils as fs
from SportsStats.Parsers.parser_utils import join_urls
from SportsStats.TimoutDetector.Timeout import *
import sys


class GetPlayersFromLinksFile:
    """
    This class loops over a provided file containing player urls
    and gets the player stats from those urls.
    """
    def __init__(self, file_path):
        # Makes a directory to store all stat files of the current character
        self.current_char = file_path.split("/")[-1][0]
        self.output_dir = f"{ALL_PLAYERS_DIR}/{self.current_char}"
        fs.try_make_dir(self.output_dir)

        self.data_lines = fs.read(file_path).split("\n")
        self.get_stats_from_urls()

    def get_stats_from_urls(self):
        for line in self.data_lines:
            if line != "":
                line = line.split(": ")
                player_name = line[0]
                player_url = join_urls(BASE_HOCKEY_URL, line[1])

                print(f"[+] Working on {player_name}", end=f"{' '*20}\r")
                sys.stdout.flush()

                player_stats = Timeout(GetPlayerStats(player_url).get_all_stats, 10).run()
                fs.write(f"{self.output_dir}/{player_name}.txt", player_stats)
