from SportsStats.GetLinks.GetPlayerLinks import *

# This file needs to be run first!

hockey_urls = GetPlayerLinks(BASE_HOCKEY_URL, mode="pro")
hockey_urls.get_all_player_urls()
