import unittest
from pychembldb import chembldb, FracClassification


class FracClassificationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(FracClassification).filter_by(frac_class_id=470).first()

    def test_active_ingredient(self):
        self.assertEqual(self.target.active_ingredient, "PEFURAZOATE")

    def test_level1(self):
        self.assertEqual(self.target.level1, "G")

    def test_level1_description(self):
        self.assertEqual(self.target.level1_description, "STEROL BIOSYNTHESIS IN MEMBRANES")

    def test_level2(self):
        self.assertEqual(self.target.level2, "G1")

    def test_level2_description(self):
        self.assertEqual(self.target.level2_description, "C14-DEMETHYLASE IN STEROL BIOSYNTHESIS (ERG11/CYP51)")

    def test_level3(self):
        self.assertEqual(self.target.level3, "G13")

    def test_level3_description(self):
        self.assertEqual(self.target.level3_description, "DMI-FUNGICIDES (DEMETHYLATION INHIBITORS) (SBI: CLASS I)")

    def test_level4(self):
        self.assertEqual(self.target.level4, "G13D")

    def test_level4_description(self):
        self.assertEqual(self.target.level4_description, "IMIDAZOLES")

    def test_level5(self):
        self.assertEqual(self.target.level5, "G13D3")

    def test_frac_code(self):
        self.assertEqual(self.target.frac_code, "3")


