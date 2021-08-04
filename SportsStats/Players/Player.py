from SportsStats.WebActions.web_actions import *
from SportsStats.settings import *


class GetPlayerStats:
    def __init__(self, player_url):
        self.player_url = player_url  # URL to the players stat page.
        self.session = Session()  # New web session.
        self.player_page = self.session.soup_request(self.player_url)  # Soups the player page.
        self.player_stats = dict()

    def get_name(self) -> str:
        """
        Extracts the players name from the H1 at the top of the page.
        :return:
        """
        return self.player_page.find("h1", {"itemprop": NAME_ITEM_PROP}).span.text

    def get_career_summary(self) -> dict:
        """
        Gets the player's career summary from the <div class="stats-pullout">
        :return:
        """
        # TODO: Make this function neater
        def get_stats_from_divs(lst) -> None:
            """
            Loops over the provided list of divs and adds key-value
            pairs to the career_summary dictionary.
            I.E {"stat-name": stat_value}
            :param lst:
            :return:
            """
            for i in range(1, len(lst)):
                current_div = lst[i]
                if current_div.h4 and current_div.p:
                    stat_name = current_div.h4.text
                    stat_value = current_div.p.text
                    career_summary[stat_name] = stat_value

        career_summary = dict()
        stats_pullout = self.player_page.find("div", class_=STATS_PULLOUT)
        soup_stats_pullout = soupify(stats_pullout)

        # Extracts the main player stats from the career summary.
        main_stats = soupify(soup_stats_pullout.find("div", class_="p1"))
        # Extracts extra stats from the career summary.
        extra_stats = soupify(soup_stats_pullout.find("div", class_="p2"))

        # Get the divs within the stats that contain the actual stat values.
        divs_main_stats = main_stats.find_all("div")
        divs_extra_stats = extra_stats.find_all("div")

        get_stats_from_divs(divs_main_stats)
        get_stats_from_divs(divs_extra_stats)
        return career_summary

    def get_basic_stats(self) -> None:
        """
        This function gets the stats from the "stats-basic-nhl" table.
        :return:
        """
        # Get the stats table
        stats_table = soupify(self.player_page.find("table", {"id": STATS_BASIC_NHL}))
        t_body = soupify(stats_table.find("tbody"))  # Get the <tbody> that contains the stats
        trs = t_body.find_all("tr")  # Gets the <tr>s that contain stats from the t_body

        for tr in trs:
            year_stats = dict()
            year = tr.th.text  # Gets the year of the stats.
            stats_row = soupify(tr)  # <tr> of stats.

            # Loops over the DATA_STAT_LIST and looks for those stat types in the stats_row.
            for data_stat in DATA_STAT_LIST:
                # Gets the <td> with the data-stat equal to the current data_stat in the loop.
                stat_td = soupify(stats_row.find("td", attrs={"data-stat": data_stat}))
                stat_value = stat_td.text

                year_stats[data_stat] = stat_value
            self.player_stats[year] = year_stats

    def set_stats_dict(self) -> None:
        """
        This function sets the key-value pairs in the self.player_stats dictionary.
        :return:
        """
        name = self.get_name()
        career_summary = self.get_career_summary()
        self.player_stats["name"] = name
        self.player_stats["summary"] = career_summary

    def get_all_stats(self) -> dict:
        self.get_career_summary()
        self.get_basic_stats()
        return self.player_stats
