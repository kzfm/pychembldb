import unittest
from pychembldb import chembldb, IracClassification


class IracClassificationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(IracClassification).filter_by(irac_class_id=1).first()

    def test_active_ingredient(self):
        self.assertEqual(self.target.active_ingredient, "HEXYTHIAZOX")

    def test_level1(self):
        self.assertEqual(self.target.level1, "C")

    def test_level1_description(self):
        self.assertEqual(self.target.level1_description, "GROWTH REGULATION")

    def test_level2(self):
        self.assertEqual(self.target.level2, "C10")

    def test_level2_description(self):
        self.assertEqual(self.target.level2_description, "MITE GROWTH INHIBITORS")

    def test_level3(self):
        self.assertEqual(self.target.level3, "C1010A")

    def test_level3_description(self):
        self.assertEqual(self.target.level3_description, "CLOFENTEZINE, HEXYTHIAZOX, DIFLOVIDAZIN")

    def test_level4(self):
        self.assertEqual(self.target.level4, "C1010A2")

    def test_irac_code(self):
        self.assertEqual(self.target.irac_code, "10A")


