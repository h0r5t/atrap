import unittest
from crawler.AtrapCrawler import AtrapCrawler


class TestAtrapCrawler(unittest.TestCase):

    def setUp(self):
        self.crawler = AtrapCrawler()

    def test_test(self):
        self.assertEqual(self.crawler.test(), "test")

    def test_product(self):
        self.assertEqual(self.crawler.product(3, 2), 6)

    def tearUp(self):
        pass
