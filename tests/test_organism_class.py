import unittest
from pychembldb import chembldb, OrganismClass


class OrganismClassTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(OrganismClass).first()

    def test_oc_id(self):
        self.assertEqual(self.target.oc_id, 1)

    def test_tax_id(self):
        self.assertEqual(self.target.tax_id, 10030L)

    def test_l1(self):
        self.assertEqual(self.target.l1, "Eukaryotes")

    def test_l2(self):
        self.assertEqual(self.target.l2, "Mammalia")

    def test_l3(self):
        self.assertEqual(self.target.l3, "Rodentia")
