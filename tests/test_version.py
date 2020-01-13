import unittest
import datetime
from pychembldb import chembldb, Version


class VersionTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Version).first()

    def test_name(self):
        self.assertEqual(self.target.name, "ChEMBL_25")

    def test_creation_date(self):
        self.assertEqual(self.target.creation_date, datetime.datetime(2018, 12, 10, 0, 0))

    def test_comments(self):
        self.assertEqual(self.target.comments, "ChEMBL Release 25")
