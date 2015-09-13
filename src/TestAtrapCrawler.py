import unittest
from crawler.AtrapCrawler import AtrapCrawler


class TestAtrapCrawler(unittest.TestCase):

    def setUp(self):
        self.crawler = AtrapCrawler()

    def test_loadApiKey(self):
        self.assertEqual(self.crawler.loadApiKey(), "BF744F29F9D033D7ED572834CC48F1E8")

    def tearUp(self):
        pass
