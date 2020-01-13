import unittest
from pychembldb import chembldb, MechanismRefs


class MechanismRefsTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(MechanismRefs).filter_by(mec_id=100).first()

    def test_ref_type(self):
        self.assertEqual(self.target.ref_type, "DailyMed")

    def test_ref_id(self):
        self.assertEqual(self.target.ref_id, "archiveid=215669")

    def test_ref_url(self):
        self.assertEqual(self.target.ref_url, "http://www.dailymed.nlm.nih.gov/dailymed/archives/fdaDrugInfo.cfm?archiveid=215669")
