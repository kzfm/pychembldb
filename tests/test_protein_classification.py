import unittest
from pychembldb import chembldb, ProteinClassification


class ProteinClassificationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ProteinClassification).first()

    def test_protein_class_id(self):
        self.assertEqual(self.target.protein_class_id, 0)

    def test_protein_class_desc(self):
        self.assertEqual(self.target.protein_class_desc, "protein class")

    def test_parent_id(self):
        self.assertEqual(self.target.parent_id, None)

    def test_pref_name(self):
        self.assertEqual(self.target.pref_name, "Protein class")

    def test_short_name(self):
        self.assertEqual(self.target.short_name, "Protein class")

    def test_definition(self):
        self.assertEqual(self.target.definition, "Root of the ChEMBL protein family classification")

