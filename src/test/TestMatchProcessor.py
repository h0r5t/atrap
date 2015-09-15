from core.MatchProcessor import MatchProcessor
import unittest


class TestMatchProcessor(unittest.TestCase):

    def test_loadRelevantPlayerIDs(self):
        id_list = MatchProcessor.loadRelevantPlayerIDs(self)
        self.assertTrue("43276219" in id_list)
