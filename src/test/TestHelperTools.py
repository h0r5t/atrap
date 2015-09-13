import unittest
from core import HelperTools
import os


class TestAtrapCrawler(unittest.TestCase):

    def test_getParentDir(self):
        path = os.path.join("a", "b", "c")
        self.assertEqual(HelperTools.getParentDir(path), os.path.abspath(os.path.join("a", "b")))
