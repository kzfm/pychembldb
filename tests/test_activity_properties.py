import unittest
from pychembldb import chembldb, ActivityProperty


class ActivityPropertyTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ActivityProperty).filter_by(ap_id=1).first()

    def test_activity_id(self):
        self.assertEqual(self.target.activity_id, 17126237)

    def test_type(self):
        self.assertEqual(self.target.type, "DATASET")

    def test_relation(self):
        self.assertEqual(self.target.relation, None)

    def test_value(self):
        self.assertEqual(self.target.value, None)

    def test_units(self):
        self.assertEqual(self.target.units, None)

    def test_text_value(self):
        self.assertEqual(self.target.text_value, "Hematology")

    def test_standard_type(self):
        self.assertEqual(self.target.standard_type, "DATASET")

    def test_standard_relation(self):
        self.assertEqual(self.target.standard_relation, None)

    def test_standard_value(self):
        self.assertEqual(self.target.standard_value, None)

    def test_standard_units(self):
        self.assertEqual(self.target.standard_units, None)

    def test_standard_text_value(self):
        self.assertEqual(self.target.standard_text_value, "Hematology")

    def test_comments(self):
        self.assertEqual(self.target.comments, None)

    def test_result_flag(self):
        self.assertEqual(self.target.result_flag, 0)

    def test_activity(self):
        self.assertEqual(self.target.activity.doc_id, 102486)


