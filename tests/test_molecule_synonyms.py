import unittest
from pychembldb import chembldb, MoleluleSynonym


class MoleluleSynonymTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(MoleluleSynonym).first()

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 51)

    def test_synonyms(self):
        self.assertEqual(self.target.synonyms, "UCL-1530")

    def test_syn_type(self):
        self.assertEqual(self.target.syn_type, "RESEARCH_CODE")

    def test_research_stem(self):
        self.assertEqual(self.target.research_stem, "UCL")
