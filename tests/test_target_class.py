import unittest
from pychembldb import chembl, TargetClass


class TargtClassTest(unittest.TestCase):
    def setUp(self):
        self.target = chembl.query(TargetClass).first()

    def test_l1(self):
        self.assertEqual(self.target.l1, "Adhesion")

    def test_l2(self):
        self.assertIsNone(self.target.l2)

    def test_l3(self):
        self.assertIsNone(self.target.l3)

    def test_l4(self):
        self.assertIsNone(self.target.l4)

    def test_l5(self):
        self.assertIsNone(self.target.l5)

    def test_l6(self):
        self.assertIsNone(self.target.l6)

    def test_l7(self):
        self.assertIsNone(self.target.l7)

    def test_l8(self):
        self.assertIsNone(self.target.l8)

    def test_target_classification(self):
        self.assertEqual(self.target.target_classification, "adhesion")
