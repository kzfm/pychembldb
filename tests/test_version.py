import unittest
import datetime
from pychembldb import chembldb, Version


class VersionTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Version).first()

    def test_name(self):
        self.assertEqual(self.target.name, "ChEMBL_16")

    def test_creation_date(self):
        self.assertEqual(self.target.creation_date, datetime.date(2013, 5, 7))

    def test_comments(self):
        self.assertEqual(self.target.comments, "ChEMBL Release 16")
