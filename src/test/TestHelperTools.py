import unittest
from core import HelperTools
import os


class TestAtrapCrawler(unittest.TestCase):

    def test_getParentDir(self):
        path = os.path.join("a", "b", "c")
        self.assertEqual(HelperTools.getParentDir(path), os.path.abspath(os.path.join("a", "b")))

    def test_getPlayersDir(self):
        atrap_dir = HelperTools.getParentDir(HelperTools.getParentDir(HelperTools.getParentDir(__file__)))
        path = os.path.join(atrap_dir, "static", "players")
        self.assertEqual(HelperTools.getPlayersDir(), path)
