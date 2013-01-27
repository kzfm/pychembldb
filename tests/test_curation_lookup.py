import unittest
from pychembldb import chembldb, CurationLookup


class CurationLookupTest(unittest.TestCase):
    def setUp(self):
        self.cur = chembldb.query(CurationLookup).first()

    def test_curated_by(self):
        self.assertEqual(self.cur.curated_by, "Autocuration")

    def test_decription(self):
        self.assertEqual(self.cur.decription, "Curated against extractor target assignment")
