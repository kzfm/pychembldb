import unittest
from pychembldb import chembldb, StructuralAlert
from datetime import datetime

class StructuralAlertTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(StructuralAlert).filter_by(alert_id=1).first()


    def test_alert_name(self):
        self.assertEqual(self.target.alert_name, "R1 Reactive alkyl halides")

    def test_smarts(self):
        self.assertEqual(self.target.smarts, "[Br,Cl,I][CX4;CH,CH2]")

    def test_molecules(self):
        self.assertEqual(len(self.target.molecules), 14128)