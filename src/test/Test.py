import os
import unittest
import sys

# ugly af :-(
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def getParentDir(dir):
    return os.path.abspath(os.path.join(dir, '..'))


if __name__ == '__main__':
    suite = unittest.TestSuite()

    test_dir = getParentDir(__file__)

    for file in os.listdir(test_dir):
        if file.startswith("Test") and file.endswith(".py"):
            a = file.replace(".py", "")
            if file != "Test":
                suite.addTest(unittest.defaultTestLoader.loadTestsFromName(a))

    unittest.TextTestRunner(verbosity=2).run(suite)
