import unittest
from core.Dota2ApiWrapper import Dota2ApiWrapper
from core.AtrapCrawler import AtrapCrawler


class TestDota2ApiWrapper(unittest.TestCase):

    def setUp(self):
        atrapCrawler = AtrapCrawler()
        self.apiWrapper = Dota2ApiWrapper(atrapCrawler.loadApiKey())

    def test_getLeagueListing(self):
        json_object = self.apiWrapper.getLeagueListing()
        self.assertTrue("result" in json_object)

    def test_getLiveLeagueGames(self):
        json_object = self.apiWrapper.getLiveLeagueGames()
        self.assertTrue("result" in json_object)

    def test_getJsonObjectForApiCall(self):
        test_url = "http://ip.jsontest.com/"
        json_object = self.apiWrapper.getJsonObjectForApiCall(test_url)
        self.assertTrue("ip" in json_object)

    def tearUp(self):
        pass
