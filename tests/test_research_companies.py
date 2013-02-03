import unittest
from pychembldb import chembldb, ResearchCompany


class ResearchCompanyTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ResearchCompany).get(1)

    def test_co_stem_id(self):
        self.assertEqual(self.target.co_stem_id, 1)

    def test_res_stem_id(self):
        self.assertEqual(self.target.res_stem_id, 646)

    def test_company(self):
        self.assertEqual(self.target.company, "Xenome")

    def test_country(self):
        self.assertEqual(self.target.country, "Australia")

    def test_previous_company(self):
        self.assertEqual(self.target.previous_company, None)

