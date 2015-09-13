import unittest
import json
import os
from core import ApiObjects
from core import HelperTools


class TestApiObjects(unittest.TestCase):

    def test_LiveLeagueGamesList(self):
        sample_json_obj = self.loadJsonFromTestFile("live_league_games_sample")
        league_games_list = ApiObjects.LiveLeagueGamesList(sample_json_obj)

        self.assertEqual(len(league_games_list.getGames()), 8)

    def test_LiveLeagueGame(self):
        sample_json_obj = self.loadJsonFromTestFile("live_league_games_sample")
        league_games_list = ApiObjects.LiveLeagueGamesList(sample_json_obj)
        league_game = league_games_list.getGames()[0]

        self.assertEqual(league_game.getMatchID(), str(1790729288))

    def test_LiveLeagueGameTeam(self):
        sample_json_obj = self.loadJsonFromTestFile("live_league_games_sample")
        league_games_list = ApiObjects.LiveLeagueGamesList(sample_json_obj)
        league_game = league_games_list.getGames()[0]
        league_team_radiant = league_game.getRadiantTeam()
        league_team_dire = league_game.getDireTeam()

        self.assertTrue(league_team_radiant is None)
        self.assertEqual(league_team_dire.getTeamName(), "Cybersport Professional LeagueRU")
        self.assertEqual(league_team_dire.getTeamID(), str(2418724))

    def loadJsonFromTestFile(self, filename):
        sample = open(os.path.join(HelperTools.getParentDir(__file__), "res", filename + ".json"), encoding="utf8")
        content = sample.read().strip()
        json_obj = json.loads(content)
        return json_obj
