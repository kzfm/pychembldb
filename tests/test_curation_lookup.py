import unittest
from pychembldb import chembl, CurationLookup


class CurationLookupTest(unittest.TestCase):
    def setUp(self):
        self.cur = chembl.query(CurationLookup).first()

    def test_curated_by(self):
        self.assertEqual(self.cur.curated_by, "Autocuration")

    def test_decription(self):
        self.assertEqual(self.cur.decription, "Curated against extractor target assignment")
