import unittest
import datetime
from pychembldb import chembl, Version


class VersionTest(unittest.TestCase):
    def setUp(self):
        self.target = chembl.query(Version).first()

    def test_name(self):
        self.assertEqual(self.target.name, "ChEMBL_14")

    def test_creation_date(self):
        self.assertEqual(self.target.creation_date, datetime.date(2012, 6, 27))

    def test_comments(self):
        self.assertEqual(self.target.comments, "ChEMBL release 14")
