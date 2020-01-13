import unittest
from pychembldb import chembldb, AtcClassification


class AtcClassificationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(AtcClassification).first()

    def test_who_name(self):
        self.assertEqual(self.target.who_name, "sodium fluoride")

    def test_level1(self):
        self.assertEqual(self.target.level1, "A")

    def test_level2(self):
        self.assertEqual(self.target.level2, "A01")

    def test_level3(self):
        self.assertEqual(self.target.level3, "A01A")

    def test_level4(self):
        self.assertEqual(self.target.level4, "A01AA")

    def test_level5(self):
        self.assertEqual(self.target.level5, "A01AA01")

    #def test_who_id(self):
    #    self.assertEqual(self.target.who_id, "who0001")

    def test_level1_description(self):
        self.assertEqual(self.target.level1_description, "ALIMENTARY TRACT AND METABOLISM")

    def test_level2_description(self):
        self.assertEqual(self.target.level2_description, "STOMATOLOGICAL PREPARATIONS")

    def test_level3_description(self):
        self.assertEqual(self.target.level3_description, "STOMATOLOGICAL PREPARATIONS")

    def test_level4_description(self):
        self.assertEqual(self.target.level4_description, "Caries prophylactic agents")
