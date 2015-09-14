import unittest
from CoverageData import CoverageData
from core import HelperTools
import os


class TestCoverageData(unittest.TestCase):

    def test_notCoveredAsString(self):
        test_list = [1, 2, 3, 5, 6, 7, 9, 10, 11]
        result = CoverageData.notCoveredAsString(self, test_list)
        self.assertEqual(result, "1 2 3 5 6 7 9 10 11")

    def test_getMethodsWithNonTestedCodeString(self):
        sample_file = os.path.join(HelperTools.getParentDir(__file__), "res",  "TestSample.test")
        test_list = [4, 13, 14]
        result = CoverageData.getMethodsWithNonTestedCodeString(self, sample_file, test_list)
        self.assertEqual(result, "test1() test3()")
