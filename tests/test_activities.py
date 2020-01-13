import unittest
from pychembldb import chembldb, Activity
from decimal import Decimal

class ActivityTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Activity).get(31863)

    def test_activity_id(self):
        self.assertEqual(self.target.activity_id, 31863)

    def test_assay_id(self):
        self.assertEqual(self.target.assay_id, 54505)

    def test_doc_id(self):
        self.assertEqual(self.target.doc_id, 6424)

    def test_record_id(self):
        self.assertEqual(self.target.record_id, 206172)

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 180094)

    def test_relation(self):
        self.assertEqual(self.target.standard_relation, ">")

#    def test_published_value(self):
#        self.assertEqual(self.target.published_value, 100.0)

#    def test_published_units(self):
#        self.assertEqual(self.target.published_units, "uM")

    def test_standard_value(self):
        self.assertEqual(self.target.standard_value, 100000.0)

    def test_standard_units(self):
        self.assertEqual(self.target.standard_units, "nM")

    def test_standard_flag(self):
        self.assertEqual(self.target.standard_flag, 1)

    def test_standard_type(self):
        self.assertEqual(self.target.standard_type, "IC50")

    def test_activity_comment(self):
        self.assertIsNone(self.target.activity_comment)

    def test_data_validity_comment(self):
        self.assertIsNone(self.target.data_validity_comment)

    def test_potential_duplicate(self):
        self.assertEqual(self.target.potential_duplicate, 0)

    def test_pchembl_value(self):
        self.assertIsNone(self.target.pchembl_value)

    def test_bao_endpoint(self):
        self.assertEqual(self.target.bao_endpoint, "BAO_0000190")

    def test_uo_units(self):
        self.assertEqual(self.target.uo_units, "UO_0000065")

    def test_qudt_units(self):
        self.assertEqual(self.target.qudt_units, "http://www.openphacts.org/units/Nanomolar")

    def test_toid(self):
        self.assertIsNone(self.target.toid)

    def test_upper_value(self):
        self.assertIsNone(self.target.upper_value)

    def test_standard_upper_value(self):
        self.assertIsNone(self.target.standard_upper_value)

    def test_src_id(self):
        self.assertEqual(self.target.src_id, 1)

    def test_type(self):
        self.assertEqual(self.target.type, "IC50")

    def test_relation(self):
        self.assertEqual(self.target.relation, ">")

    def test_value(self):
        self.assertEqual(self.target.value, Decimal('100.0'))

    def test_units(self):
        self.assertEqual(self.target.units, "uM")

    def test_text_value(self):
        self.assertIsNone(self.target.text_value)

    def test_standard_text_value(self):
        self.assertIsNone(self.target.standard_text_value)


