from SportsStats.Players.GetPlayersFromLinksFile import *


char = input("[+] Which group of players do you want to get? [a, b, c...z] ")
file = fs.get_dir_files(f"{LINKS_DIR}/{char}")
GetPlayersFromLinksFile(file)
