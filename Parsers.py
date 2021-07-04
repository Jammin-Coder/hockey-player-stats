#!/usr/bin/python3

import funcs
from bs4 import BeautifulSoup

funcs = funcs.MyFuncs()


class StatsParser:
    def parse_meta(self, stats_page):
        meta = funcs.soupify(stats_page.find("div", id="meta"))
        data_div = funcs.soupify(meta.find("div", itemtype="https://schema.org/Person"))
        p_tags = data_div.find_all("p")
        for tag in p_tags:
            yield tag.text

    def get_nhl_standard(self, stats_page):
        overheader_adjictives = []
        overheader_dict = {}
        standard_table = stats_page.find("table", id="stats_basic_plus_nhl")
        thead_rows = standard_table.find_all("tr")
        overheaders = thead_rows[0].find_all("th")
        headers = thead_rows[1].find_all("th")
        for i in range(len(overheaders)):
            text = overheaders[i].text
            if not text == "":
                overheader_adjictives.append(text)
        overheader_string = f"\t\t|\t{overheader_adjictives[0]}\t    | {overheader_adjictives[1]} \t| {overheader_adjictives[2]}| {overheader_adjictives[3]}\t| {overheader_adjictives[4]}"
        print(overheader_string)
        header_string = ""
        for header in headers:
            header_string += header.text + " "
        print(header_string)


    def get_summary(self, stats_page):
        career_summary = []
        stats_pullout = stats_page.find("div", class_="stats_pullout")
        stats_div = funcs.soupify(stats_pullout)
        paragraph1 = stats_div.find("div", class_="p1").find_all("div")
        paragraph2 = stats_div.find("div", class_="p2").find_all("div")

        # Get career summary
        for div in paragraph1:
            div = funcs.soupify(div)
            stat = div.h4.text
            stat_value = div.p.text
            career_summary.append({"stat": stat, "value": stat_value})
        for div in paragraph2:
            div = funcs.soupify(div)
            stat = div.h4.text
            stat_value = div.p.text
            career_summary.append({"stat": stat, "value": stat_value})

        out_text1 = "Career Summary\n"
        out_text2 = "----------------------------------\n"
        out_text3 = ""

        for item in career_summary:
            out_text3 += f"{item['stat']}\t{item['value']}\n"

        parsed_summary = out_text1 + out_text2 + out_text3
        return parsed_summary
