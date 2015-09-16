from core.MatchProcessor import MatchProcessor
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
import os
from core import HelperTools


class TestMatchProcessor(unittest.TestCase):

    @patch("core.MatchProcessor.HelperTools")
    def test_loadLocalPlayer(self, MockHelperTools):
        players_test_dir = os.path.join(HelperTools.getParentDir(__file__), "res",  "players_test")
        MockHelperTools.getPlayersDir = MagicMock(return_value=players_test_dir)
        mp = MatchProcessor()
        local_player_obj = mp.loadLocalPlayer("21232132")
        self.assertEquals(local_player_obj.getPlayerID(), 21232132)
