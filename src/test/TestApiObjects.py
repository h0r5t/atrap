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

    def test_MatchDetails(self):
        sample_json_obj = self.loadJsonFromTestFile("sample_match_details")
        match_details_obj = ApiObjects.MatchDetails(sample_json_obj)
        players_list = match_details_obj.players

        self.assertEqual(len(players_list), 10)
        self.assertEqual(match_details_obj.getMatchID(), "1789503761")
        self.assertTrue(match_details_obj.getRadiantWin())
        self.assertEqual(match_details_obj.getLeagueID(), "3502")

    def test_MatchDetailsPlayer(self):
        sample_json_obj = self.loadJsonFromTestFile("sample_match_details")
        match_details_obj = ApiObjects.MatchDetails(sample_json_obj)
        players_list = match_details_obj.getPlayers()
        first_player = players_list[0]
        first_player_acc_id = "87360406"
        self.assertEqual(first_player.getAccountID(), first_player_acc_id)
        self.assertTrue(first_player.wasOnRadiant())
        self.assertFalse(players_list[9].wasOnRadiant())
        self.assertEqual(first_player.getKills(), "13")
        self.assertEqual(first_player.getDeaths(), "5")
        self.assertEqual(first_player.getAssists(), "14")
        self.assertEqual(first_player.getLastHits(), "580")
        self.assertEqual(first_player.getGPM(), "686")
        self.assertEqual(first_player.getXPM(), "549")
        self.assertEqual(first_player.getTowerDamage(), "2464")
        self.assertEqual(first_player.getHeroDamage(), "18417")
        self.assertEqual(first_player.getHeroHealing(), "0")

    def loadJsonFromTestFile(self, filename):
        sample = open(os.path.join(HelperTools.getParentDir(__file__), "res", filename + ".json"), encoding="utf8")
        content = sample.read().strip()
        json_obj = json.loads(content)
        return json_obj
