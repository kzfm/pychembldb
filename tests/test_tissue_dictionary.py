import unittest
from pychembldb import chembldb, TissueDictionary
from datetime import datetime

class TissueDictionaryTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(TissueDictionary).filter_by(uberon_id="UBERON:0000007").first()


    def test_pref_name(self):
        self.assertEqual(self.target.pref_name, "Pituitary gland")

    def test_efo_id(self):
        self.assertEqual(self.target.efo_id, "UBERON:0000007")

    def test_bto_id(self):
        self.assertEqual(self.target.bto_id, "BTO:0001073")

    def test_caloha_id(self):
        self.assertEqual(self.target.caloha_id, "TS-0798")

    def test_assays(self):
        self.assertEqual(len(self.target.assays), 183)