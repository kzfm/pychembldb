import unittest
from pychembldb import chembldb, MetabolismRefs


class MetabolismRefsTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(MetabolismRefs).filter_by(met_id=120).first()

    def test_ref_type(self):
        self.assertEqual(self.target.ref_type, "OTHER")

    def test_ref_id(self):
        self.assertEqual(self.target.ref_id, "http://www.accessdata.fda.gov/drugsatfda_docs/nda/99/50-778_Ellence_biopharmr.pdf")

    def test_ref_url(self):
        self.assertEqual(self.target.ref_url, "http://www.accessdata.fda.gov/drugsatfda_docs/nda/99/50-778_Ellence_biopharmr.pdf")
