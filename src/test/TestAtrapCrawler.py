import unittest
from unittest.mock import MagicMock
from core.AtrapCrawler import AtrapCrawler
from core.ApiObjects import LiveLeagueGamesList
from core import HelperTools
import json


class TestAtrapCrawler(unittest.TestCase):

    def test_loadApiKey(self):
        crawler = AtrapCrawler()
        self.assertEqual(crawler.loadApiKey(), "BF744F29F9D033D7ED572834CC48F1E8")

    def test_loadConfig(self):
        crawler = AtrapCrawler()
        config = crawler.loadConfig()
        self.assertTrue(len(config) > 0)

    def test_getRelevantLiveLeagueGames(self):
        team_id_filter_list = ["2183640", "2526992", "1477137"]
        games_list = LiveLeagueGamesList(self.loadJsonFromTestFile("live_league_games_sample")).getGames()

        crawler = AtrapCrawler()
        crawler.api_wrapper.getLiveLeagueGames = MagicMock(return_value=games_list)

        relevant_games = crawler.getRelevantLiveLeagueGames(team_id_filter_list)
        match_id_list = []
        for game in relevant_games:
            match_id_list.append(str(game.getMatchID()))

        self.assertTrue("1790745997" in match_id_list)
        self.assertTrue("1790669081" in match_id_list)
        self.assertTrue("1790750102" in match_id_list)

    def test_loadTeams(self):
        crawler = AtrapCrawler()
        teams_json = crawler.loadTeams()
        self.assertTrue(len(teams_json) > 2)

    def test_genereateTeamIDList(self):
        crawler = AtrapCrawler()
        teams_json = self.loadJsonFromTestFile("static_team_list_sample")
        id_list = crawler.genereateTeamIDList(teams_json)
        self.assertTrue("1838315" in id_list)
        self.assertTrue("39" in id_list)
        self.assertTrue("36" in id_list)

    def loadJsonFromTestFile(self, filename):
        sample = open(HelperTools.getParentDir(__file__) + "\\res\\" + filename + ".json", encoding="utf8")
        content = sample.read().strip()
        json_obj = json.loads(content)
        return json_obj
