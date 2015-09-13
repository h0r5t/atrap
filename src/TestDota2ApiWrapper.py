import unittest
from crawler.Dota2ApiWrapper import Dota2ApiWrapper
from crawler.AtrapCrawler import AtrapCrawler


class TestDota2ApiWrapper(unittest.TestCase):

    def setUp(self):
        atrapCrawler = AtrapCrawler()
        self.apiWrapper = Dota2ApiWrapper(atrapCrawler.loadApiKey())

    def test_getLeagueListing(self):
        json_object = self.apiWrapper.getLeagueListing()
        self.assertTrue(True)

    def tearUp(self):
        pass
