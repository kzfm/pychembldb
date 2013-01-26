import unittest
from pychembldb import chembl, AssayType


class AssayTypeTest(unittest.TestCase):
    def setUp(self):
        self.target = chembl.query(AssayType).first()

    def test_assay_type(self):
        self.assertEqual(self.target.assay_type, "A")

    def test_assay_desc(self):
        self.assertEqual(self.target.assay_desc, "ADMET")

# too slow but pass the test
#    def test_assays(self):
#        self.assertEqual(self.target.assays[0].chembl_id, "CHEMBL884521")
