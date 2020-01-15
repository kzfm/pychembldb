import unittest
from pychembldb import chembldb, BioassayOntology


class BioassayOntologyTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(BioassayOntology).filter_by(bao_id="BAO_0000006").first()

    def test_label(self):
        self.assertEqual(self.target.label, "percent cytotoxicity")
