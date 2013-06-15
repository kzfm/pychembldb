import unittest
from pychembldb import chembldb, Domain


class DomainTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Domain).first()

    def test_domain_id(self):
        self.assertEqual(self.target.domain_id, 2627L)

    def test_domain_type(self):
        self.assertEqual(self.target.domain_type, "Pfam-A")

    def test_source_domain_id(self):
        self.assertEqual(self.target.source_domain_id, "PF00001")

    def test_domain_name(self):
        self.assertEqual(self.target.domain_name, "7tm_1")

    def test_domain_description(self):
        self.assertEqual(self.target.domain_description, None)

    def test_sites(self):
        self.assertEqual(len(self.target.sites), 320)

    def test_componentdomains(self):
        self.assertEqual(len(self.target.componentdomains), 569)

    def test_domains(self):
        self.assertEqual(len(self.target.components), 565)
