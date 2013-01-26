import unittest
from pychembldb import chembl, Source


class SourceTest(unittest.TestCase):
    def setUp(self):
        self.target = chembl.query(Source).get(3)

    def test_src_id(self):
        self.assertEqual(self.target.src_id, 3)

    def test_src_description(self):
        self.assertEqual(self.target.src_description, "Novartis Malaria Screening")

    def test_src_assays(self):
        self.assertEqual(len(self.target.assays), 6)

    # todo compound_records-relationship
