import unittest
from pychembldb import chembldb, BioComponentSequence


class BioComponentSequenceTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(BioComponentSequence).first()

    def test_component_id(self):
        self.assertEqual(self.target.component_id, 6287)

    def test_component_type(self):
        self.assertEqual(self.target.component_type, "PROTEIN")

    def test_description(self):
        self.assertEqual(self.target.description, "Tigatuzumab heavy chain")

    def test_sequence(self):
        self.assertEqual(self.target.sequence[:10], "EVQLVESGGG")

    def test_sequence_md5sum(self):
        self.assertEqual(self.target.sequence_md5sum, "72c2e91eedf4fbbfbb8f9581fe8f50cc")

    def test_tax_id(self):
        self.assertEqual(self.target.tax_id, None)

    def test_organism(self):
        self.assertEqual(self.target.organism, None)

