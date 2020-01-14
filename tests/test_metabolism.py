import unittest
from pychembldb import chembldb, Metabolism


class MetabolismTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Metabolism).filter_by(met_id=783).first()

    def test_pathway_id(self):
        self.assertEqual(self.target.pathway_id, 1)

    def test_pathway_key(self):
        self.assertEqual(self.target.pathway_key, None)

    def test_enzyme_name(self):
        self.assertEqual(self.target.enzyme_name, "CYP2C19")

    def test_met_conversion(self):
        self.assertEqual(self.target.met_conversion, "Hydroxylation")

    def test_organism(self):
        self.assertEqual(self.target.organism, None)

    def test_met_comment(self):
        self.assertEqual(self.target.met_comment[:20], "Organ: Liver and Int")

    def test_refs(self):
        self.assertEqual(len(self.target.refs), 1)

