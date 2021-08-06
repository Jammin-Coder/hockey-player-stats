from SportsStats.Players.GetPlayersFromLinksFile import *


char = input("[+] Which group of players do you want to get? [a, b, c...z] ")
link_file = f"{LINKS_DIR}/{char}.txt"
GetPlayersFromLinksFile(link_file)
