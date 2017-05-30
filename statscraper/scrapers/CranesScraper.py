# encoding: utf-8
""" A scraper to fetch daily cranes sightings at Hornborgasjön
    from http://web05.lansstyrelsen.se/transtat_O/transtat.asp
    This is intended to be a minimal example of a scraper
    using Beautiful Soup.
"""
import requests
from bs4 import BeautifulSoup
from statscraper import BaseScraper, Dataset, Dimension


class Cranes(BaseScraper):

    def _fetch_itemslist(self):
        """There is only one dataset"""
        yield Dataset("Number of cranes")

    def _fetch_dimensions(self):
        """ Declaring available dimensions like this is not mandatory,
         but nice, especially if they differ from dataset to dataset.
        """
        yield Dimension(u"date")
        yield Dimension(u"month")
        yield Dimension(u"year")

    def _fetch_data(self, query=None):
        html = requests.get("http://web05.lansstyrelsen.se/transtat_O/transtat.asp").text
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find("table", "line").find_all("table")[2].findNext("table")
        rows = table.find_all("tr")
        column_headers = rows.pop(0).find_all("td", recursive=False)
        years = [x.text for x in column_headers[2:]]
        for row in rows:
            cells = row.find_all("td")
            date = cells.pop(0).text
            month = cells.pop(0).text
            i = 0
            for value in cells:
                yield {
                    "date": date,
                    "month": month,
                    "year": years[i],
                    "value": value.text,
                }
                i += 1