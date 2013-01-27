import unittest
from pychembldb import chembldb, ConfidenceScore


class ConfidenceScoreTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ConfidenceScore).first()

    def test_confidence_score(self):
        self.assertEqual(self.target.confidence_score, 0)

    def test_description(self):
        self.assertEqual(self.target.description, "Default value - Target unknown or has yet to be assigned")

    def test_target_mapping(self):
        self.assertEqual(self.target.target_mapping, "Unassigned")
