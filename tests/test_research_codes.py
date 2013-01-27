import unittest
from pychembldb import chembldb, ResearchCode


class ResearchCodeTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ResearchCode).first()

    def test_stem(self):
        self.assertEqual(self.target.stem, "4SC")

    def test_company(self):
        self.assertEqual(self.target.company, "4SC")

    def test_country(self):
        self.assertEqual(self.target.country, "Germany")

    def test_previous_company(self):
        self.assertIsNone(self.target.previous_company)
