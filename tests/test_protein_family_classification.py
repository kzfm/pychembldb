import unittest
from pychembldb import chembldb, ProteinFamilyClassification
from datetime import datetime

class ProteinFamilyClassificationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ProteinFamilyClassification).filter_by(protein_class_id=1).first()

    def test_l1(self):
        self.assertEqual(self.target.l1, "Enzyme")

    def test_l2(self):
        self.assertEqual(self.target.l2, None)

    def test_l3(self):
        self.assertEqual(self.target.l3, None)

    def test_l4(self):
        self.assertEqual(self.target.l4, None)

    def test_l5(self):
        self.assertEqual(self.target.l5, None)

    def test_l6(self):
        self.assertEqual(self.target.l6, None)

    def test_l7(self):
        self.assertEqual(self.target.l7, None)

    def test_l8(self):
        self.assertEqual(self.target.l8, None)

    def test_protein_class_desc(self):
        self.assertEqual(self.target.protein_class_desc, "enzyme")
