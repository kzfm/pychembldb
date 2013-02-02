import unittest
from pychembldb import chembldb, DataValidity


class DataValidityTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(DataValidity).first()

    def test_data_validity_comment(self):
        self.assertEqual(self.target.data_validity_comment, "Manually validated")

    def test_description(self):
        self.assertEqual(self.target.description, "Data have been checked against the publication and are believed to be accurate")

