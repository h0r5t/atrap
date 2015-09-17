import unittest
from core.LocalObjects import LocalPlayer
from core import LocalObjects
from core import HelperTools
import os


class TestLocalObjects(unittest.TestCase):

    def test_Local_Player(self):
        par_dir = HelperTools.getParentDir(__file__)
        path = os.path.join(par_dir, "res",  "players_test", "47434686.json")
        path2 = os.path.join(par_dir, "res",  "players_test", "21232132.json")
        player_obj = LocalPlayer(path)
        player_obj2 = LocalPlayer(path2)

        self.assertEqual(player_obj.getAverageKDA(), 0)

        self.assertFalse(player_obj2.isEmpty())
        self.assertEqual(player_obj2.getAverageGPM(), 630)
        self.assertEqual(player_obj2.getAverageXPM(), 200)
        self.assertEqual(player_obj2.getTeamName(), "TestTeam")
        self.assertEqual(player_obj2.getPlayerName(), "h0r5t")
        self.assertEqual(player_obj2.getAverageLHPM(), 8.42)
        self.assertEqual(player_obj2.getAverageTowerDamage(), 2333)
        self.assertEqual(player_obj2.getAverageHeroDamage(), 21000)
        self.assertEqual(player_obj2.getCounter(), 23)

    def test_AverageValues(self):
        pass

    def test_updateAverage(self):
        old_average = 0
        count = 0
        val = 50
        self.assertEqual(LocalObjects.updateAverage(old_average, count, val), 50)
