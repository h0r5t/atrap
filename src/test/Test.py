import os
import unittest
import sys
import coverage
from CoverageData import CoverageData
import io


# ugly af :-(
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def getParentDir(dira):
    return os.path.abspath(os.path.join(dira, '..'))


if __name__ == '__main__':

    suite = unittest.TestSuite()

    test_dir = getParentDir(__file__)

    for file in os.listdir(test_dir):
        if file.startswith("Test") and file.endswith(".py"):
            a = file.replace(".py", "")
            if file != "Test":
                suite.addTest(unittest.defaultTestLoader.loadTestsFromName(a))

    coverage = coverage.coverage()
    coverage.start()

    stream = io.StringIO()
    unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)

    coverage.stop()
    coverageData = CoverageData(coverage)
    print("--------------\n")
    for string in coverageData.getCoverageData():
        print(string)
    print("\n--------------")
