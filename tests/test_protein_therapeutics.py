import unittest
from pychembldb import chembldb, ProteinTherapeutic


class ProteinTherapeuticTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ProteinTherapeutic).first()

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 48705L)

    def test_protein_description(self):
        self.assertEqual(self.target.protein_description, "Oxytocin-neurophysin 1 [Precursor]")

    def test_protein_sequence(self):
        self.assertEqual(self.target.protein_sequence[:10], "MAGPSLACCL")

    def test_protein_species(self):
        self.assertEqual(self.target.protein_species, "Homo sapiens")

    def test_protein_sequence_length(self):
        self.assertEqual(self.target.protein_sequence_length, 125L)

    def test_mature_peptide_sequence(self):
        self.assertIsNone(self.target.mature_peptide_sequence)
