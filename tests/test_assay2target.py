import unittest
from pychembldb import chembldb, Assay2Target


class Assay2TargetTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Assay2Target).filter_by(assay_id=1000).first()

    def test_assay_id(self):
        self.assertEqual(self.target.assay_id, 1000)

    def test_tid(self):
        self.assertEqual(self.target.tid, 51)

    def test_relationship_type(self):
        self.assertEqual(self.target.relationship_type, "D")

    def test_complex(self):
        self.assertEqual(self.target.complex, 0)

    def test_multi(self):
        self.assertEqual(self.target.multi, 0)

    def test_confidence_score(self):
        self.assertEqual(self.target.confidence_score, 9)

    def test_curated_by(self):
        self.assertEqual(self.target.curated_by, "Expert")
