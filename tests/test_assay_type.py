import unittest
from pychembldb import chembldb, AssayType


class AssayTypeTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(AssayType).first()

    def test_assay_type(self):
        self.assertEqual(self.target.assay_type, "A")

    def test_assay_desc(self):
        self.assertEqual(self.target.assay_desc, "ADME")

# too slow but pass the test
#    def test_assays(self):
#        self.assertEqual(self.target.assays[0].chembl_id, "CHEMBL884521")
