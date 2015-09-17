import sys
import unittest
from test import EndToEndTest
import logging


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr)
    logging.getLogger("EndToEndTest").setLevel(logging.DEBUG)
    logging.getLogger("api").setLevel(logging.DEBUG)
    logging.getLogger("logs").setLevel(logging.DEBUG)
    suite = unittest.TestSuite()
    suite.addTest(unittest.defaultTestLoader.loadTestsFromModule(EndToEndTest))
    unittest.TextTestRunner(verbosity=2, stream=sys.stderr).run(suite)
