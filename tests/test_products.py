import unittest
import datetime
from pychembldb import chembldb, Product


class ProductTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Product).filter_by(trade_name="PAREDRINE").first()

    def test_dosage_form(self):
        self.assertEqual(self.target.dosage_form, "SOLUTION/DROPS")

    def test_route(self):
        self.assertEqual(self.target.route, "OPHTHALMIC")

    def test_trade_name(self):
        self.assertEqual(self.target.trade_name, "PAREDRINE")

    def test_approval_date(self):
        self.assertEqual(self.target.approval_date, datetime.date(1982, 1, 1))

    def test_ad_type(self):
        self.assertEqual(self.target.ad_type, "DISCN")

    def test_oral(self):
        self.assertEqual(self.target.oral, 0)

    def test_topical(self):
        self.assertEqual(self.target.topical, 1)

    def test_parenteral(self):
        self.assertEqual(self.target.parenteral, 0)

    #def test_information_source(self):
    #    self.assertEqual(self.target.information_source, "CDER")

    def test_black_box_warning(self):
        self.assertIsNone(self.target.black_box_warning)

    def test_applicant_full_name(self):
        self.assertEqual(self.target.applicant_full_name, "PHARMICS INC")

    def test_innovator_company(self):
        self.assertEqual(self.target.innovator_company, 0)

    def test_product_id(self):
        self.assertEqual(self.target.product_id, "PRODUCT_000004_004")

    def test_formulations(self):
        self.assertEqual(len(self.target.formulations), 1)

    def test_formulations_ingredient(self):
        self.assertEqual(self.target.formulations[0].ingredient, "HYDROXYAMPHETAMINE HYDROBROMIDE")
