import unittest
from CoverageData import CoverageData


class TestCoverageData(unittest.TestCase):

    def test_notCoveredAsString(self):
        list = [1, 2, 3, 5, 6, 7, 9, 10, 11]
        result = CoverageData.notCoveredAsString(self, list)
        self.assertEqual(result, "1 2 3 5 6 7 9 10 11")
