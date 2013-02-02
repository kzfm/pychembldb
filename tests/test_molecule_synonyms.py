import unittest
from pychembldb import chembldb, MoleculeSynonym


class MoleluleSynonymTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(MoleculeSynonym).first()

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 97)

    def test_synonyms(self):
        self.assertEqual(self.target.synonyms, "CP-12299")

    def test_syn_type(self):
        self.assertEqual(self.target.syn_type, "RESEARCH_CODE")

    def test_research_stem(self):
        self.assertEqual(self.target.research_stem.research_stem, "CP")
