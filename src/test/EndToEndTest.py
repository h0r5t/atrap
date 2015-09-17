import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
import os
from core import HelperTools
from core.ApiObjects import MatchDetails
from core.AtrapCrawler import AtrapCrawler
import json
import logging
from core.ApiObjects import LiveLeagueGamesList


class EndToEndTest(unittest.TestCase):

    def setUp(self):
        ete_dir = os.path.join(getParentDir(__file__), "res",  "end_to_end_test")
        fake_players_dir = os.path.join(ete_dir, "web", "live", "players")
        fake_matches_dir = os.path.join(ete_dir, "web", "live", "matches")
        fake_avg_carry = os.path.join(ete_dir, "web", "avg", "carry", "average_values.json")
        fake_avg_sup = os.path.join(ete_dir, "web", "avg", "support", "average_values.json")
        fake_avg_mid = os.path.join(ete_dir, "web", "avg", "mid", "average_values.json")
        fake_avg_off = os.path.join(ete_dir, "web", "avg", "offlane", "average_values.json")

        for f in os.listdir(fake_players_dir):
            os.remove(os.path.join(fake_players_dir, f))

        for f in os.listdir(fake_matches_dir):
            os.remove(os.path.join(fake_matches_dir, f))

        os.remove(fake_avg_carry)
        os.remove(fake_avg_sup)
        os.remove(fake_avg_mid)
        os.remove(fake_avg_off)

    @patch("core.AtrapCrawler.HelperTools")
    @patch("core.LocalObjects.HelperTools")
    @patch("core.ApiObjects.HelperTools")
    def test_end_to_end(self, HelperToolsMock3, HelperToolsMock2, HelperToolsMock):
        ete_dir = os.path.join(getParentDir(__file__), "res",  "end_to_end_test")
        match_id = "1790745997"

        fake_teams_file = os.path.join(ete_dir, "teams.json")
        fake_players_dir = os.path.join(ete_dir, "web", "live", "players")
        api_key_file = os.path.join(getParentDir(getParentDir(getParentDir(__file__))), "config", "api_key.key")
        fake_matches_dir = os.path.join(ete_dir, "matches")
        fake_cfg = os.path.join(ete_dir, "config.cfg")
        fake_web_dir = os.path.join(ete_dir, "web")
        fake_match_file = os.path.join(ete_dir, "web", "live", "matches", match_id + ".json")

        HelperToolsMock2.getMatchFile = MagicMock(return_value=fake_match_file)
        HelperToolsMock.getTeamsFile = MagicMock(return_value=fake_teams_file)
        HelperToolsMock.getPlayersDir = MagicMock(return_value=fake_players_dir)
        HelperToolsMock.getApiKeyFile = MagicMock(return_value=api_key_file)
        HelperToolsMock.getMatchesDir = MagicMock(return_value=fake_matches_dir)
        HelperToolsMock.getConfigFile = MagicMock(return_value=fake_cfg)
        HelperToolsMock.getWebDir = MagicMock(return_value=fake_web_dir)
        HelperToolsMock.log = myLog

        HelperToolsMock2.getMatchFile = MagicMock(return_value=fake_match_file)
        HelperToolsMock2.getTeamsFile = MagicMock(return_value=fake_teams_file)
        HelperToolsMock2.getPlayersDir = MagicMock(return_value=fake_players_dir)
        HelperToolsMock2.getApiKeyFile = MagicMock(return_value=api_key_file)
        HelperToolsMock2.getMatchesDir = MagicMock(return_value=fake_matches_dir)
        HelperToolsMock2.getConfigFile = MagicMock(return_value=fake_cfg)
        HelperToolsMock2.getWebDir = MagicMock(return_value=fake_web_dir)
        HelperToolsMock2.log = myLog

        HelperToolsMock3.HelperToolsMock2.getMatchFile = MagicMock(return_value=fake_match_file)

        crawler = AtrapCrawler()

        fake_wrapper = FakeDota2ApiWrapper(crawler)
        crawler.api_wrapper = fake_wrapper
        crawler.start()


class FakeDota2ApiWrapper():

    def __init__(self, crawler):
        self.crawler = crawler

        self.counter1 = 6
        self.json_sample_1 = LiveLeagueGamesList(self.loadJsonFromTestFile("live_league_games_sample")).getGames()
        self.json_sample_2 = LiveLeagueGamesList(self.loadJsonFromTestFile("live_league_games_sample_2")).getGames()

        self.match_details = MatchDetails(self.loadJsonFromTestFile("match_details_end_to_end"))
        self.log = logging.getLogger("api")

    def getLiveLeagueGames(self):
        self.counter1 -= 1
        if self.counter1 > 3:
            return self.json_sample_1
        if self.counter1 == 3:
            return self.json_sample_2
        if self.counter1 < 0:
            self.crawler.stop()
            return self.json_sample_2

    def getMatchDetails(self, match_id):
        return self.match_details

    def loadJsonFromTestFile(self, filename):
        sample = open(os.path.join(HelperTools.getParentDir(__file__), "res", filename + ".json"), encoding="utf8")
        content = sample.read().strip()
        json_obj = json.loads(content)
        return json_obj


def getParentDir(dira):
    return os.path.abspath(os.path.join(dira, '..'))


def saveJsonToFile(json_obj, path):
    json.dump(json_obj, path, sort_keys=True, indent=4, separators=(',', ': '))


def side_effect(*args):
    path = str(args[0])
    log = logging.getLogger("logs")
    log.debug("load: " + path)
    if not os.path.isfile(path):
        return {}
    sample = open(path, encoding="utf8")
    content = sample.read().strip()
    if (content == ""):
        return {}
    json_obj = json.loads(content)
    return json_obj


def myLog(string):
    log = logging.getLogger("logs")
    log.debug(string)
