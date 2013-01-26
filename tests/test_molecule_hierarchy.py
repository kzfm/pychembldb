import unittest
from pychembldb import chembl, MoleluleHierarchy


class MoleluleHierarchyTest(unittest.TestCase):
    def setUp(self):
        self.target = chembl.query(MoleluleHierarchy).first()

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 1)

    def test_parent_molregno(self):
        self.assertEqual(self.target.parent_molregno, 1)

    def test_active_molregno(self):
        self.assertEqual(self.target.active_molregno, 1)
