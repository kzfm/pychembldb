import unittest
from pychembldb import chembldb, GOClassification
from datetime import datetime

class GOClassificationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(GOClassification).filter_by(go_id="GO:0000003").first()

    def test_parent_go_id(self):
        self.assertEqual(self.target.parent_go_id, "GO:0008150")

    def test_pref_name(self):
        self.assertEqual(self.target.pref_name, "reproduction")

    def test_class_level(self):
        self.assertEqual(self.target.class_level, 1)

    def test_aspect(self):
        self.assertEqual(self.target.aspect, "P")

    def test_path(self):
        self.assertEqual(self.target.path, "biological_process  reproduction")

    def test_components(self):
        self.assertEqual(len(self.target.components), 11)