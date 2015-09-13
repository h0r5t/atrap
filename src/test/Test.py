import os
import unittest
import sys

# ugly af :-(
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if __name__ == '__main__':
    suite = unittest.TestSuite()

    for file in os.listdir('./src/test/'):
        if file.startswith("Test") and file.endswith(".py"):
            a = file.replace(".py", "")
            if file != "Test":
                suite.addTest(unittest.defaultTestLoader.loadTestsFromName(a))

    unittest.TextTestRunner(verbosity=2).run(suite)
