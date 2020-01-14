import unittest
from pychembldb import chembldb, ProductPatent
from datetime import datetime

class ProductPatentTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ProductPatent).filter_by(prod_pat_id=270).first()

    def test_patentno(self):
        self.assertEqual(self.target.patent_no, "8133883")

    def test_patent_expire_date(self):
        self.assertEqual(self.target.patent_expire_date, datetime(2023, 4, 14, 0, 0))

    def test_drug_substance_flag(self):
        self.assertEqual(self.target.drug_substance_flag, 0)

    def test_drug_product_flag(self):
        self.assertEqual(self.target.drug_product_flag, 1)

    def test_delist_flag(self):
        self.assertEqual(self.target.delist_flag, 0)