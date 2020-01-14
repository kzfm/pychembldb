import unittest
from pychembldb import chembldb, PatentUseCode


class PatentUseCodeTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(PatentUseCode).filter_by(patent_use_code="U-943").first()

    def test_definition(self):
        self.assertEqual(self.target.definition[:20], "GNRH ANTAGONIST INDI")

    def test_products(self):
        self.assertEqual(len(self.target.products), 2)

    def test_patents(self):
        self.assertEqual(len(self.target.patents), 2)