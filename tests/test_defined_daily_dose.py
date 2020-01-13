import unittest
from pychembldb import chembldb, DefinedDailyDose
from decimal import Decimal


class DefinedDailyDoseTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(DefinedDailyDose).filter_by(atc_code="A01AA01").first()

    def test_atc_code(self):
        self.assertEqual(self.target.atc_code, "A01AA01")

    def test_ddd_value(self):
        self.assertEqual(self.target.ddd_value, Decimal('1.10'))

    def test_ddd_units(self):
        self.assertEqual(self.target.ddd_units, "mg")

    def test_ddd_admr(self):
        self.assertEqual(self.target.ddd_admr, "O")

    def test_ddd_comment(self):
        self.assertEqual(self.target.ddd_comment, "0.5 mg fluoride")

    def test_ddd_id(self):
        self.assertEqual(self.target.ddd_id, 2166)
