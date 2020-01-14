import unittest
from pychembldb import chembldb, HracClassification


class HracClassificationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(HracClassification).filter_by(hrac_class_id=1).first()

    def test_active_ingredient(self):
        self.assertEqual(self.target.active_ingredient, "CLODINAFOP-PROPARGYL")

    def test_level1(self):
        self.assertEqual(self.target.level1, "A")

    def test_level1_description(self):
        self.assertEqual(self.target.level1_description, "INHIBITION OF ACETYL COA CARBOXYLASE (ACCASE)")

    def test_level2(self):
        self.assertEqual(self.target.level2, "A1")

    def test_level2_description(self):
        self.assertEqual(self.target.level2_description, "ARYLOXYPHENOXY-PROPIONATE 'FOPS'")

    def test_level3(self):
        self.assertEqual(self.target.level3, "A11")

    def test_hrac_code(self):
        self.assertEqual(self.target.hrac_code, "A")


