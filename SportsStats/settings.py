"""
This file contains constants that are used throughout the program.
"""

HTML_PARSER = "lxml"  # HTML parser that is used by BeautifulSoup

BASE_HOCKEY_URL = "https://www.hockey-reference.com/"

# DIRECTORY PATHS
DATA_DIR = "data"  # Directory where the data is stored.
LINKS_DIR = f"{DATA_DIR}/links"  # Path to file where links are stored
ALL_PLAYERS_DIR = f"{DATA_DIR}/players"


# Fixed URL paths
PLAYERS_PATH = "/players/"


# Content IDs ####
PAGE_INDEX = "page_index"
DIV_PLAYERS = "div_players"
ALL_PLAYERS = "all_players"

# Content classes ####
STATS_PULLOUT = "stats_pullout"

# Stats table IDs
STATS_BASIC_PLUS_NHL = "stats_basic_plus_nhl"

# This is the name of the H1 that contains the players name on the stats page.
NAME_ITEM_PROP = "name"


# List of stat-types to target in the player-stats page
DATA_STAT_LIST = ["age", "team_id", "lg_id", "games_played",
                  "goals", "assists", "points", "plus_minus",
                  "pen_min", "goals_ev", "goals_pp", "goals_sh",
                  "goals_gw", "assists_ev", "assists_pp", "assists_sh",
                  "shots", "shot_pct", "time_on_ice", "time_on_ice_avg", "award_summary"]

