import unittest
from pychembldb import chembldb, LigandEff
from decimal import Decimal


class LigandEffTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(LigandEff).first()

    def test_activity_id(self):
        self.assertEqual(self.target.activity_id, 31864)

    def test_bei(self):
        self.assertEqual(self.target.bei, Decimal('14.06'))

    def test_sei(self):
        self.assertEqual(self.target.sei, Decimal('5.56'))

    def test_le(self):
        self.assertEqual(self.target.le, Decimal('0.26'))

    def test_lle(self):
        self.assertEqual(self.target.lle, Decimal('1.30'))