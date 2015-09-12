import os
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite()

    for file in os.listdir('./src/'):
        if file.startswith("Test") and file.endswith(".py"):
            a = file.replace(".py", "")
            if file != "Test":
                suite.addTest(unittest.defaultTestLoader.loadTestsFromName(a))

    unittest.TextTestRunner(verbosity=2).run(suite)
