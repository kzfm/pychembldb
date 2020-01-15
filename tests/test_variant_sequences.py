import unittest
from pychembldb import chembldb, VariantSequence
from datetime import datetime

class VariantSequenceTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(VariantSequence).filter_by(variant_id=109).first()


    def test_mutation(self):
        self.assertEqual(self.target.mutation, "H203A")

    def test_accession(self):
        self.assertEqual(self.target.accession, "Q14994")

    def test_version(self):
        self.assertEqual(self.target.version, 2)

    def test_isoform(self):
        self.assertEqual(self.target.isoform, 2)

    def test_sequence(self):
        self.assertEqual(self.target.sequence[:20], "MASREDELRNCVVCGDQATG")

    def test_organism(self):
        self.assertEqual(self.target.organism, "Homo sapiens")

    def test_assays(self):
        self.assertEqual(len(self.target.assays), 2)