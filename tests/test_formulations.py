import unittest
from pychembldb import chembldb, Formulation


class FormulationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Formulation).filter_by(product_id="PRODUCT_017641_001").filter_by(molregno=674619).first()

    def test_product_id(self):
        self.assertEqual(self.target.product_id, "PRODUCT_017641_001")

    def test_ingredient(self):
        self.assertEqual(self.target.ingredient, "CALCIUM CHLORIDE")

    def test_strength(self):
        self.assertEqual(self.target.strength, "20MG/100ML")

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 674619)

    def test_formulation_backref(self):
        self.assertEqual(self.target.molecule.pref_name, "CALCIUM CHLORIDE")
