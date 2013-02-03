import unittest
from pychembldb import chembldb, ActivityStd


class ActivityStdTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ActivityStd).get(1)

    def test_std_act_id(self):
        self.assertEqual(self.target.std_act_id, 1)

    def test_standard_type(self):
        self.assertEqual(self.target.standard_type, "CC50")

    def test_definition(self):
        self.assertEqual(self.target.definition, "Concentration required for 50% cytotoxicity")

    def test_standard_units(self):
        self.assertEqual(self.target.standard_units, "nM")

    def test_normal_range_min(self):
        self.assertEqual(self.target.normal_range_min, 1.0)

    def test_normal_range_max(self):
        self.assertEqual(self.target.normal_range_max, 10000000.0)

