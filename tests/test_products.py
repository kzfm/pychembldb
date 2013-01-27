import unittest
from pychembldb import chembldb, Product


class ProductTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Product).first()

    def test_dosage_form(self):
        self.assertIsNone(self.target.dosage_form)

    def test_route(self):
        self.assertIsNone(self.target.route)

    def test_trade_name(self):
        self.assertEqual(self.target.trade_name, "REMICADE")

    def test_approval_date(self):
        self.assertIsNone(self.target.approval_date)

    def test_ad_type(self):
        self.assertIsNone(self.target.ad_type)

    def test_oral(self):
        self.assertEqual(self.target.oral, 0)

    def test_topical(self):
        self.assertEqual(self.target.topical, 0)

    def test_parenteral(self):
        self.assertEqual(self.target.parenteral, 1)

    def test_information_source(self):
        self.assertEqual(self.target.information_source, "CDER")

    def test_black_box_warning(self):
        self.assertIsNone(self.target.black_box_warning)

    def test_applicant_full_name(self):
        self.assertEqual(self.target.applicant_full_name, "CENTOCOR INC")

    def test_innovator_company(self):
        self.assertIsNone(self.target.innovator_company)

    def test_product_id(self):
        self.assertEqual(self.target.product_id, "PRODUCT19072")

    def test_formulations(self):
        self.assertEqual(len(self.target.formulations), 1)

    def test_formulations_ingredient(self):
        self.assertEqual(self.target.formulations[0].ingredient, "INFLIXIMAB")
