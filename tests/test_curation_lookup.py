import unittest
from pychembldb import chembldb, Curation


class CurationLookupTest(unittest.TestCase):
    def setUp(self):
        self.cur = chembldb.query(Curation).first()

    def test_curated_by(self):
        self.assertEqual(self.cur.curated_by, "Autocuration")

    def test_decription(self):
        self.assertEqual(self.cur.description, "Curated against extractor target assignment")
