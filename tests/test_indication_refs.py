import unittest
from pychembldb import chembldb, IndicationRefs


class IndicationRefsTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(IndicationRefs).filter_by(drugind_id=22612).first()

    def test_drugind_id(self):
        self.assertEqual(self.target.drugind_id, 22612)

    def test_ref_type(self):
        self.assertEqual(self.target.ref_type, "ATC")

    def test_ref_id(self):
        self.assertEqual(self.target.ref_id, "A10BF01")

    def test_ref_url(self):
        self.assertEqual(self.target.ref_url, "http://www.whocc.no/atc_ddd_index/?code=A10BF01")
