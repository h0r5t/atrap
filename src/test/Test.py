from __future__ import print_function
import os
import unittest
import sys
import coverage
from CoverageData import CoverageData

# ugly af :-(
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def getParentDir(dira):
    return os.path.abspath(os.path.join(dira, '..'))


if __name__ == '__main__':

    run_coverage = False

    suite = unittest.TestSuite()

    test_dir = getParentDir(__file__)

    for file in os.listdir(test_dir):
        if file.startswith("Test") and file.endswith(".py"):
            a = file.replace(".py", "")
            if file != "Test":
                suite.addTest(unittest.defaultTestLoader.loadTestsFromName(a))

    if run_coverage:
        coverage = coverage.coverage()
        coverage.start()

    unittest.TextTestRunner(verbosity=2, stream=sys.stdout).run(suite)

    if run_coverage:
        coverage.stop()
        coverageData = CoverageData(coverage)
        print("--------------\n")
        for string in coverageData.getCoverageData():
            print(string)
        print("\n--------------")


def warning(warning):
    # print("WARNING: ", warning, file=sys.stderr)
    pass
