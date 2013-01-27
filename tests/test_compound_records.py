import unittest
from pychembldb import chembldb, CompoundRecord


class CompoundRecordTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(CompoundRecord).first()

    def test_record_id(self):
        self.assertEqual(self.target.record_id, 1)

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 41)

    def test_doc_id(self):
        self.assertEqual(self.target.doc_id, 11788)

    def test_compound_key(self):
        self.assertEqual(self.target.compound_key, "X")

    def test_compound_name(self):
        self.assertEqual(self.target.compound_name, "Bis(3-[14-Benzyl-11-(1H-indol-3-ylmethyl)-2-isobutyl-13-methyl-5-(2-methylsulfanyl-ethyl)-3,6,9,12,15,20-hexaoxo-1,4,7,10,13,16-hexaaza-bicyclo[15.2.1]icos-18-en-8-yl]-propionamide)")

    def test_src_id(self):
        self.assertEqual(self.target.src_id, 1)

    def test_src_compound_id(self):
        self.assertIsNone(self.target.src_compound_id)

    # comopund-activities
    def test_activities(self):
        self.assertEqual(len(self.target.activities), 3)

    def test_activities_backref(self):
        self.assertEqual(self.target.activities[0].record_id, self.target.record_id)
