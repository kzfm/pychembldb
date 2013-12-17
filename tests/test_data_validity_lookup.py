import unittest
from pychembldb import chembldb, DataValidity


class DataValidityTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(DataValidity).first()

    def test_data_validity_comment(self):
        self.assertEqual(self.target.data_validity_comment, "Author confirmed error")

    def test_description(self):
        self.assertEqual(self.target.description, "Error in publication - Author confirmed (personal communication)")

