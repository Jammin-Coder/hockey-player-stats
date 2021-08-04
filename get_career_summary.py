from SportsStats.Players.Player import *


stats = GetPlayerStats("https://www.hockey-reference.com/players/c/coffepa01.html")

career_summary = stats.get_career_summary()
print(career_summary)
