import unittest
from pychembldb import chembldb, LigandEff


class LigandEffTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(LigandEff).first()

    def test_activity_id(self):
        self.assertEqual(self.target.activity_id, 31864L)

    def test_bei(self):
        self.assertEqual(self.target.bei, 14.06)

    def test_sei(self):
        self.assertEqual(self.target.sei, 5.56)
