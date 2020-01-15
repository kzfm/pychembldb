import unittest
from pychembldb import chembldb, AssayClassification
from datetime import datetime

class AssayClassificationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(AssayClassification).filter_by(assay_class_id=1).first()

    def test_l1(self):
        self.assertEqual(self.target.l1, "ALIMENTARY TRACT AND METABOLISM")

    def test_l2(self):
        self.assertEqual(self.target.l2, "Anti-Obesity Activity")

    def test_l3(self):
        self.assertEqual(self.target.l3, "Computer-Assisted Measurement of Food Consumption in Rats Anorectic Activity")

    def test_class_type(self):
        self.assertEqual(self.target.class_type, "In vivo efficacy")

    def test_source(self):
        self.assertEqual(self.target.source, "Vogel_2008")

    def test_assays(self):
        self.assertEqual(len(self.target.assays), 0)