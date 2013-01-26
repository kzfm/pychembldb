import unittest
from pychembldb import chembl, Assay


class AssayTest(unittest.TestCase):
    def setUp(self):
        self.target = chembl.query(Assay).get(10)

    def test_assay_id(self):
        self.assertEqual(self.target.assay_id, 10)

    def test_assay_type(self):
        self.assertEqual(self.target.assay_type, "F")

    def test_description(self):
        self.assertEqual(self.target.description, "In vitro cell cytotoxicity against 143B-LTK cell lines expressed in HSV-1 TK")

    def test_doc_id(self):
        self.assertEqual(self.target.doc_id, 17430L)

    def test_src_id(self):
        self.assertEqual(self.target.src_id, 1)

    def test_src_assay_id(self):
        self.assertIsNone(self.target.src_assay_id)

    def test_chembl_id(self):
        self.assertEqual(self.target.chembl_id, "CHEMBL615126")

    def test_assay_category(self):
        self.assertIsNone(self.target.assay_category)

    def test_assay_organism(self):
        self.assertEqual(self.target.assay_organism, "Homo sapiens")

    def test_assay_tax_id(self):
        self.assertEqual(self.target.assay_tax_id, 9606L)

    def test_assay_strain(self):
        self.assertIsNone(self.target.assay_strain)

    # assay -> assay_type
    def test_assay_type_backref(self):
        self.assertEqual(self.target.type.assay_desc, "Functional")

#    def test_assay_targets(self):
#        self.assertEqual(len(self.target.targets), 0)
