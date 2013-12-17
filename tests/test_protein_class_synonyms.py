import unittest
from pychembldb import chembldb, ProteinClassSynonym


class ProteinClassSynonimTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ProteinClassSynonym).first()

    def test_protein_classsyn_id(self):
        self.assertEqual(self.target.protein_class_id, 1)

    def test_protein_class_id(self):
        self.assertEqual(self.target.protein_class_id, 1)

    def test_protein_class_synonym(self):
        self.assertEqual(self.target.protein_class_synonym, "Enzyme")

    def test_syn_type(self):
        self.assertEqual(self.target.syn_type, "CONCEPT_WIKI")
