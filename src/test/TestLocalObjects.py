import unittest
from core.LocalObjects import LocalPlayer
from core import HelperTools
import os


class TestLocalObjects(unittest.TestCase):

    def test_Local_Player(self):
        par_dir = HelperTools.getParentDir(__file__)
        path = os.path.join(par_dir, "res",  "players_test", "43276219.json")
        player_obj = LocalPlayer(path)
        self.assertTrue(player_obj.isEmpty())
