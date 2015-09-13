import unittest
import json
from core import ApiObjects
from core import HelperTools


class TestApiObjects(unittest.TestCase):

    def setUp(self):
        sample_json_obj = self.loadJsonFromTestFile("live_league_games_sample")
        self.league_games_list = ApiObjects.LiveLeagueGamesList(sample_json_obj)
        self.league_game = self.league_games_list.getGames()[0]
        self.league_team_radiant = self.league_game.getRadiantTeam()
        self.league_team_dire = self.league_game.getDireTeam()

    def test_LiveLeagueGamesList(self):
        self.assertEqual(len(self.league_games_list.getGames()), 8)

    def test_LiveLeagueGame(self):
        self.assertEqual(self.league_game.getMatchID(), str(1790729288))

    def test_LiveLeagueGameTeam(self):
        self.assertTrue(self.league_team_radiant is None)
        self.assertEqual(self.league_team_dire.getTeamName(), "Cybersport Professional LeagueRU")
        self.assertEqual(self.league_team_dire.getTeamID(), str(2418724))

    def loadJsonFromTestFile(self, filename):
        sample = open(HelperTools.getParentDir(__file__) + "\\res\\" + filename + ".json")
        content = sample.read().strip()
        json_obj = json.loads(content)
        return json_obj

    def tearUp(self):
        pass
