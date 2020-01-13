import unittest
from pychembldb import chembldb, Cell


class CellTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Cell).get(1)

    def test_cell_id(self):
        self.assertEqual(self.target.cell_id, 1)

    def test_cell_name(self):
        self.assertEqual(self.target.cell_name, "DC3F")

    def test_cell_description(self):
        self.assertEqual(self.target.cell_description, "DC3F")

    def test_cell_source_tissue(self):
        self.assertEqual(self.target.cell_source_tissue, "Lung")

    def test_cell_source_organism(self):
        self.assertEqual(self.target.cell_source_organism, "Cricetulus griseus")

    def test_cell_source_tax_id(self):
        self.assertEqual(self.target.cell_source_tax_id, 10029)

    def test_clo_id(self):
        self.assertEqual(self.target.clo_id, None)

    def test_efo_id(self):
        self.assertEqual(self.target.efo_id, None)

    def test_cellosaurus_id(self):
        self.assertEqual(self.target.cellosaurus_id, "CVCL_4704")

    def test_cl_lincs_id(self):
        self.assertEqual(self.target.cl_lincs_id, None)

    def test_cembl_id(self):
        self.assertEqual(self.target.chembl_id, "CHEMBL3307241")

