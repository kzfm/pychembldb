import unittest
from pychembldb import chembldb, PredictedBindingDomain


class PredictedBindingDomainTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(PredictedBindingDomain).get(1)

    def test_predbind_id(self):
        self.assertEqual(self.target.predbind_id, 1)

    def test_activity_id(self):
        self.assertEqual(self.target.activity_id, 470000L)

    def test_site_id(self):
        self.assertEqual(self.target.site_id, 1620)

    def test_prediction_method(self):
        self.assertEqual(self.target.prediction_method, "Single domain")

    def test_confidence(self):
        self.assertEqual(self.target.confidence, "high")
