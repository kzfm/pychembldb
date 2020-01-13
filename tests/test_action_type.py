import unittest
from pychembldb import chembldb, ActionType


class ActionTypeTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ActionType).first()

    def test_description(self):
        self.assertEqual(self.target.description[:20], "Positively effects t")

    def test_parent_type(self):
        self.assertEqual(self.target.parent_type, "POSITIVE MODULATOR")

    def test_mechanisms(self):
        self.assertEqual(len(self.target.mechanisms), 42)

