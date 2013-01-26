import unittest
from pychembldb import chembl, DefinedDailyDose


class DefinedDailyDoseTest(unittest.TestCase):
    def setUp(self):
        self.target = chembl.query(DefinedDailyDose).first()

    def test_atc_code(self):
        self.assertEqual(self.target.atc_code, "A01AA01")

    def test_ddd_value(self):
        self.assertEqual(self.target.ddd_value, 1.1)

    def test_ddd_units(self):
        self.assertEqual(self.target.ddd_units, "mg")

    def test_ddd_admr(self):
        self.assertEqual(self.target.ddd_admr, "O")

    def test_ddd_comment(self):
        self.assertEqual(self.target.ddd_comment, "0.5 mg Fluoride")

    def test_ddd_id(self):
        self.assertEqual(self.target.ddd_id, 1)
