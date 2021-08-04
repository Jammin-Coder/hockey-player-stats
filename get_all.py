from SportsStats.Players.Player import *
from SportsStats.FileSystem.file_system_utils import *


json_file = read_json(LINKS_JSON_FILE)

base_url = json_file["base_link"]

chars = "abcdefghijklmnopqrstuvwyz"

stats_dict = dict()

for char in chars:
    stats_dict[char] = dict()
    links = json_file[char]
    for key in links.keys():
        name = key
        full_url = base_url + links[name]
        print(f"Working on {name}.")
        stat_getter = GetPlayerStats(full_url)
        stats = stat_getter.get_all_stats()
        stats_dict[name] = stats
    break

del_file_content(DATA_JSON_FILE)
write_json(DATA_JSON_FILE, stats_dict)
