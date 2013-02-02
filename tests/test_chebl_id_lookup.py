import unittest
from pychembldb import chembldb, ChemblId


class ChemblIdLookupTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ChemblId).first()

    def test_chembl_id(self):
        self.assertEqual(self.target.chembl_id, "CHEMBL1")

    def test_entity_type(self):
        self.assertEqual(self.target.entity_type, "COMPOUND")

    def test_entity_id(self):
        self.assertEqual(self.target.entity_id, 517180)

    def test_status(self):
        self.assertEqual(self.target.status, "ACTIVE")
