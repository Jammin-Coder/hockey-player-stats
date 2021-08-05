from .GetPlayersFromLinksFile import *


class GetAllPlayerStats:
    def __init__(self):
        self.url_files = fs.get_dir_files(LINKS_DIR)
        self.get_all_stats()

    def get_all_stats(self):
        for file in self.url_files:
            GetPlayersFromLinksFile(file)
