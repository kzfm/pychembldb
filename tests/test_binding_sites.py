import unittest
from pychembldb import chembldb, BindingSite


class BindingSiteTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(BindingSite).filter_by(site_name="Mu opioid receptor, 7tm_1 domain").first()

    def test_site_id(self):
        self.assertEqual(self.target.site_id, 17)

    def test_site_name(self):
        self.assertEqual(self.target.site_name, "Mu opioid receptor, 7tm_1 domain")

    def test_tid(self):
        self.assertEqual(self.target.tid, 12471)

#    def test_sitecomponents(self):
#        self.assertEqual(len(self.target.sitecomponents), 1)

    def test_predicted_binding_domains(self):
        self.assertEqual(len(self.target.predicted_binding_domains), 524)

#    def test_components(self):
#        self.assertEqual(len(self.target.components), 1)

#    def test_domains(self):
#        self.assertEqual(len(self.target.domains), 1)
