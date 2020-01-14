import unittest
from pychembldb import chembldb, StructuralAlertSet
from datetime import datetime

class StructuralAlertSetTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(StructuralAlertSet).filter_by(alert_set_id=1).first()


    def test_set_name(self):
        self.assertEqual(self.target.set_name, "Glaxo")

    def test_priority(self):
        self.assertEqual(self.target.priority, 8)

    def test_alerts(self):
        self.assertEqual(len(self.target.alerts), 55)