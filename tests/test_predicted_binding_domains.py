import unittest
from pychembldb import chembldb, PredictedBindingDomain


class PredictedBindingDomainTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(PredictedBindingDomain).filter_by(site_id=1620).first()

    def test_predbind_id(self):
        self.assertEqual(self.target.predbind_id, 2532444)

    def test_activity_id(self):
        self.assertEqual(self.target.activity_id, 397754)

    def test_site_id(self):
        self.assertEqual(self.target.site_id, 1620)

    def test_prediction_method(self):
        self.assertEqual(self.target.prediction_method, "Single domain")

    def test_confidence(self):
        self.assertEqual(self.target.confidence, "high")
