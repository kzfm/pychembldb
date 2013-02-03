import unittest
from pychembldb import chembldb, SiteComponent


class SiteComponentTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(SiteComponent).get(1)

    def test_sitecomp_id(self):
        self.assertEqual(self.target.sitecomp_id, 1)

    def test_site_id(self):
        self.assertEqual(self.target.site_id, 838)

    def test_component_id(self):
        self.assertEqual(self.target.component_id, 4819)

    def test_domain_id(self):
        self.assertEqual(self.target.domain_id, 3172)

    def test_site_residues(self):
        self.assertEqual(self.target.site_residues, None)
