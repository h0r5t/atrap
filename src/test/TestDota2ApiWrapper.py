import unittest
from core.Dota2ApiWrapper import Dota2ApiWrapper
from core.AtrapCrawler import AtrapCrawler
import time
import os
import json
from unittest.mock import MagicMock
from core import HelperTools


class TestDota2ApiWrapper(unittest.TestCase):

    def setUp(self):
        atrapCrawler = AtrapCrawler()
        self.apiWrapper = Dota2ApiWrapper(atrapCrawler.loadApiKey())

    def test_getLeagueListing(self):
        faked_json = self.loadJsonFromTestFile("league_listing_sample")
        self.apiWrapper.getJsonObjectForApiCall = MagicMock(return_value=faked_json)
        json_object = self.apiWrapper.getLeagueListing()
        self.assertTrue("result" in json_object)

    def test_getLiveLeagueGames(self):
        faked_json = self.loadJsonFromTestFile("live_league_games_sample")
        self.apiWrapper.getJsonObjectForApiCall = MagicMock(return_value=faked_json)
        live_league_games = self.apiWrapper.getLiveLeagueGames()
        self.assertTrue(live_league_games is not None)

    def test_getJsonObjectForApiCall(self):
        # test_url = "http://ip.jsontest.com/"
        # json_object = self.apiWrapper.getJsonObjectForApiCall(test_url)
        # self.assertTrue("ip" in json_object)

        bad_url = "https://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/V001/"
        json_object = self.apiWrapper.getJsonObjectForApiCall(bad_url)
        self.assertTrue(len(json_object) == 0)
        time.sleep(1)

    def test_getMatchDetails(self):
        faked_json = self.loadJsonFromTestFile("sample_match_details")
        self.apiWrapper.getJsonObjectForApiCall = MagicMock(return_value=faked_json)
        match_details_object = self.apiWrapper.getMatchDetails("id_does_not_matter")
        self.assertTrue(match_details_object is not None)

    def loadJsonFromTestFile(self, filename):
        sample = open(os.path.join(HelperTools.getParentDir(__file__), "res", filename + ".json"), encoding="utf8")
        content = sample.read().strip()
        json_obj = json.loads(content)
        return json_obj
