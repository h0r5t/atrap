from core.MatchProcessor import MatchProcessor
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import os
from core import HelperTools


class TestMatchProcessor(unittest.TestCase):

    @patch("core.MatchProcessor.HelperTools")
    def test_loadRelevantPlayerIDs(self, MockHelperTools):
        players_test_dir = os.path.join(HelperTools.getParentDir(__file__), "res",  "players_test")
        MockHelperTools.getPlayersDir = MagicMock(return_value=players_test_dir)
        id_list = MatchProcessor.loadRelevantPlayerIDs(self)
        self.assertTrue("43276219" in id_list)
        self.assertTrue("21232132" in id_list)

    @patch("core.MatchProcessor.HelperTools")
    def test_loadLocalPlayers(self, MockHelperTools):
        players_test_dir = os.path.join(HelperTools.getParentDir(__file__), "res",  "players_test")
        MockHelperTools.getPlayersDir = MagicMock(return_value=players_test_dir)
        mp = MatchProcessor()
        player_list = mp.loadLocalPlayers()
        self.assertTrue(len(player_list) == 2)
