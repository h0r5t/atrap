import unittest
from crawler.Dota2ApiWrapper import Dota2ApiWrapper


class TestDota2ApiWrapper(unittest.TestCase):

    def setUp(self):
        self.apiWrapper = Dota2ApiWrapper()

    def test_test(self):
        self.assertEqual(self.apiWrapper.test(), "test")

    def tearUp(self):
        pass
