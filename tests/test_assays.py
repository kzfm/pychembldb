import unittest
from pychembldb import chembldb, Assay


class AssayTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Assay).get(10)

    def test_assay_id(self):
        self.assertEqual(self.target.assay_id, 10)

    def test_assay_type(self):
        self.assertEqual(self.target.assay_type, "F")

    def test_assay_test_type(self):
        self.assertIsNone(self.target.assay_test_type)

    def test_description(self):
        self.assertEqual(self.target.description, "In vitro cell cytotoxicity against 143B-LTK cell lines expressed in HSV-1 TK")

    def test_doc_id(self):
        self.assertEqual(self.target.doc_id, 17430)

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
        self.assertEqual(self.target.assay_tax_id, 9606)

    def test_assay_strain(self):
        self.assertIsNone(self.target.assay_strain)

    def test_assay_tissue(self):
        self.assertIsNone(self.target.assay_tissue)

    def test_assay_cell_type(self):
        self.assertEqual(self.target.assay_cell_type, "143B-LTK")

    def test_assay_subcellular_fraction(self):
        self.assertIsNone(self.target.assay_subcellular_fraction)

    def test_src_assay_id(self):
        self.assertIsNone(self.target.src_assay_id)

    def test_aidx(self):
        self.assertEqual(self.target.aidx, "CLD0")

    # assay -> assay_type
    def test_assay_type_backref(self):
        self.assertEqual(self.target.type.assay_desc, "Functional")

    # assay -> activity
    def test_assay_activities(self):
        self.assertEqual(len(self.target.activities), 7)

    def test_assay_activities_backref(self):
        self.assertEqual(self.target.activities[0].assay.assay_id, 10)
