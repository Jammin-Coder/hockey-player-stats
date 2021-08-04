from SportsStats.GetLinks.GetPlayerLinks import *

hockey_urls = GetPlayerLinks("https://www.hockey-reference.com/", mode="pro")
hockey_urls.get_all_player_urls()
