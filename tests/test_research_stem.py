import unittest
from pychembldb import chembldb, ResearchStem


class ResearchStemTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ResearchStem).first()

    def test_res_stem_id(self):
        self.assertEqual(self.target.res_stem_id, 2)

    def test_research_stem(self):
        self.assertEqual(self.target.research_stem, "4SC")

    def test_synonyms(self):
        self.assertEqual(len(self.target.synonyms), 0)

    def test_companies(self):
        self.assertEqual(len(self.target.companies), 1)
