import unittest
from pychembldb import chembldb, ActivitySupp


class ActivitySuppTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ActivitySupp).filter_by(as_id=1).first()

    def test_rgid(self):
        self.assertEqual(self.target.rgid, 1)

    def test_smid(self):
        self.assertEqual(self.target.smid, 1012613)

    def test_type(self):
        self.assertEqual(self.target.type, "Liver_Deposit, glycogen (Peripheral)")

    def test_relation(self):
        self.assertEqual(self.target.relation, None)

    def test_value(self):
        self.assertEqual(self.target.value, None)

    def test_units(self):
        self.assertEqual(self.target.units, None)

    def test_text_value(self):
        self.assertEqual(self.target.text_value, "slight")

    def test_standard_type(self):
        self.assertEqual(self.target.standard_type, "Liver_Deposit, glycogen (Peripheral)")

    def test_standard_relation(self):
        self.assertEqual(self.target.standard_relation, None)

    def test_standard_value(self):
        self.assertEqual(self.target.standard_value, None)

    def test_standard_units(self):
        self.assertEqual(self.target.standard_units, None)

    def test_standard_text_value(self):
        self.assertEqual(self.target.standard_text_value, "slight")

    def test_comments(self):
        self.assertEqual(self.target.comments, "SAMPLE_ID: 0698011; SP_FLG: true; BARCODE: No ChipData")