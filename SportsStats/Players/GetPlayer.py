from SportsStats.WebActions.web_actions import *
from SportsStats.settings import *


class GetPlayerStats:
    def __init__(self, player_url):
        self.player_url = player_url  # URL to the players stat page.
        self.session = Session()  # New web session.
        self.player_page = self.session.soup_request(self.player_url)  # Soups the player page.
        self.stat_str = f"{self.get_name()}\n"

    def get_name(self) -> str:
        """
        Extracts the players name from the H1 at the top of the page.
        :return:
        """
        try:
            return self.player_page.find("h1", {"itemprop": NAME_ITEM_PROP}).span.text
        except AttributeError:
            print(f"No name for {self.player_url}")

    def get_career_summary(self):
        """
        Gets the player's career summary from the <div class="stats-pullout">
        :return:
        """

        career_summary = "Career Summary:\n"

        def get_stats_from_divs(lst) -> iter:
            for i in range(1, len(lst)):
                current_div = lst[i]
                if current_div.strong and current_div.p:
                    stat_name = current_div.strong.text
                    stat_value = current_div.p.text
                    yield f"{stat_name}: {stat_value}"

        stats_pullout = self.player_page.find("div", class_=STATS_PULLOUT)
        soup_stats_pullout = soupify(stats_pullout)

        # Extracts the main player stats from the career summary.
        main_stats = soupify(soup_stats_pullout.find("div", class_="p1"))
        # Extracts extra stats from the career summary.
        extra_stats = soupify(soup_stats_pullout.find("div", class_="p2"))

        # Get the divs within the stats that contain the actual stat values.
        divs_main_stats = main_stats.find_all("div")
        divs_extra_stats = extra_stats.find_all("div")
        # Main and extra stats generator objects
        main_stats = get_stats_from_divs(divs_main_stats)
        extra_stats = get_stats_from_divs(divs_extra_stats)

        # Loop over the stats generator objects and append stat to career_summary
        for stat in main_stats:
            career_summary += f"\t{stat}\n"

        for stat in extra_stats:
            career_summary += f"\t{stat}\n"

        self.stat_str += career_summary

    def get_basic_stats(self) -> None:
        """
        This function gets the stats from the "stats-basic-nhl" table and puts
        them into self.stat_str.
        :return:
        """

        self.stat_str += "\nCareer Stats:"

        # Get the stats table
        stats_table = self.player_page.find("table", {"id": STATS_BASIC_PLUS_NHL})

        # TODO: If no basic stats stable found, try to find another stats table.
        if not stats_table:
            self.stat_str += "\n\tNo basic stats available.\n\tThis will be fixed in later version."
            return

        soup_stats_table = soupify(stats_table)
        t_body = soupify(soup_stats_table.find("tbody"))  # Get the <tbody> that contains the stats
        trs = t_body.find_all("tr")  # Gets the <tr>s that contain stats from the t_body

        for tr in trs:
            year = tr.th.text  # Gets the year of the stats.
            self.stat_str += f"\n\tYear: {year}\n"
            stats_row = soupify(tr)  # <tr> of stats.

            # Loops over the DATA_STAT_LIST and looks for those stat types in the stats_row.
            for data_stat in DATA_STAT_LIST:
                # Gets the <td> with the data-stat equal to the current data_stat in the loop.
                stat_td = soupify(stats_row.find("td", attrs={"data-stat": data_stat}))
                stat_value = stat_td.text
                self.stat_str += f"\t\t{data_stat}: {stat_value}\n"

    def get_all_stats(self) -> str:
        self.get_career_summary()
        self.get_basic_stats()
        return self.stat_str
