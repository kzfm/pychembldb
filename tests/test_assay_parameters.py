import unittest
from pychembldb import chembldb, AssayParameter


class AssayParameterTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(AssayParameter).filter_by(assay_param_id=3710885).first()

    def test_type(self):
        self.assertEqual(self.target.type, "immobilization_buffer_composition")

    def test_relation(self):
        self.assertEqual(self.target.relation, None)

    def test_value(self):
        self.assertEqual(self.target.value, None)
    
    def test_units(self):
        self.assertEqual(self.target.units, None)
    
    def test_text_value(self):
        self.assertEqual(self.target.text_value, "HBSN 7,4")
    
    def test_standard_type(self):
        self.assertEqual(self.target.standard_type, "immobilization_buffer_composition")
    
    def test_standard_relation(self):
        self.assertEqual(self.target.standard_relation, None)
    
    def test_standard_value(self):
        self.assertEqual(self.target.standard_value, None)
    
    def test_standard_units(self):
        self.assertEqual(self.target.standard_units, None)
    
    def test_standard_text_value(self):
        self.assertEqual(self.target.standard_text_value, "HBSN 7,4")
    
    def test_comments(self):
        self.assertEqual(self.target.comments, None)

