import unittest
from pychembldb import chembldb, Activity


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
        self.assertEqual(self.target.molregno, 180094L)

    def test_relation(self):
        self.assertEqual(self.target.standard_relation, ">")

    def test_published_value(self):
        self.assertEqual(self.target.published_value, 100.0)

    def test_published_units(self):
        self.assertEqual(self.target.published_units, "uM")

    def test_standard_value(self):
        self.assertEqual(self.target.standard_value, 100000.0)

    def test_standard_units(self):
        self.assertEqual(self.target.standard_units, "nM")

    def test_standard_type(self):
        self.assertEqual(self.target.standard_type, "IC50")

    def test_activity_comment(self):
        self.assertIsNone(self.target.activity_comment)

    def test_published_activity_type(self):
        self.assertEqual(self.target.published_type, "IC50")

    def test_predicted_binding_site(self):
        self.assertIsNone(self.target.predicted_binding_domain)

    def test_le(self):
        self.assertIsNone(self.target.le)
