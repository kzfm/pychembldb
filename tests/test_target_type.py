import unittest
from pychembldb import chembldb, TargetType


class TargtTypeTest(unittest.TestCase):
    def setUp(self):
        self.target_type = chembldb.query(TargetType).first()

    def test_target_type(self):
        self.assertEqual(self.target_type.target_type, "ADMET")

    def test_target_desc(self):
        self.assertEqual(self.target_type.target_desc, "Target is not applicable for an ADMET assay (e.g., physchem property)")

    def test_target_relation(self):
        self.assertEqual(len(self.target_type.targets), 1)
