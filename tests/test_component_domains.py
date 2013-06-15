import unittest
from pychembldb import chembldb, ComponentDomain


class ComponentDomainTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ComponentDomain).first()

    def test_compd_id(self):
        self.assertEqual(self.target.compd_id, 63)

    def test_domain_id(self):
        self.assertEqual(self.target.domain_id, 4400)

    def test_component_id(self):
        self.assertEqual(self.target.component_id, 3996)

    def test_start_position(self):
        self.assertEqual(self.target.start_position, 457)

    def test_end_position(self):
        self.assertEqual(self.target.end_position, 474)

