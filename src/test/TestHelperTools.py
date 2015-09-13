import unittest
from core import HelperTools


class TestAtrapCrawler(unittest.TestCase):

    def setUp(self):
        pass

    def test_getParentDir(self):
        path = "C:/a/b/c/"
        self.assertEqual(HelperTools.getParentDir(path).replace("\\", "/"), "C:/a/b")

    def tearUp(self):
        pass
