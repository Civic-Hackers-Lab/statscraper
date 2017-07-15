# encoding: utf-8

from unittest import TestCase
from statscraper.scrapers.work_injury_scraper import WorkInjuries


class TestInjuries(TestCase):

    def setup_method(self, test_method):
        self.scraper = WorkInjuries()

    def test_can_fetch(self):
        dataset = self.scraper[1]  # "Arbetssjukdomar"
        data = dataset.data
        self.assertTrue(len(data))
