import unittest
from pychembldb import chembldb, Doc


class DocTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Doc).get(10)

    def test_doc_id(self):
        self.assertEqual(self.target.doc_id, 10)

    def test_journal(self):
        self.assertEqual(self.target.journal, "J. Med. Chem.")

    def test_year(self):
        self.assertEqual(self.target.year, "2004")

    def test_volume(self):
        self.assertEqual(self.target.volume, "47")

    def test_issue(self):
        self.assertEqual(self.target.issue, "1")

    def test_first_page(self):
        self.assertEqual(self.target.first_page, "196")

    def test_last_page(self):
        self.assertEqual(self.target.last_page, "209")

    def test_pubmed_id(self):
        self.assertEqual(self.target.pubmed_id, 14695833L)

    def test_doi(self):
        self.assertIsNone(self.target.doi)

    def test_chembl_id(self):
        self.assertEqual(self.target.chembl_id, "CHEMBL1148467")

    def test_title(self):
        self.assertIsNone(self.target.title)

    def test_doc_type(self):
        self.assertEqual(self.target.doc_type, "PUBLICATION")

    # doc-assay
    def test_doc_assays(self):
        self.assertEqual(len(self.target.assays), 5)

    def test_doc_assays_doc(self):
        self.assertEqual(self.target.assays[0].doc.doc_id, self.target.doc_id)

    # doc-activities
    def test_doc_activities(self):
        self.assertEqual(len(self.target.activities), 90)

    def test_doc_activities_backref(self):
        self.assertEqual(self.target.activities[0].doc.doc_id, self.target.doc_id)

    # doc-compound_records
    def test_doc_compound_records(self):
        self.assertEqual(len(self.target.compounds), 54)

    def test_doc_compound_records_backref(self):
        self.assertEqual(self.target.compounds[0].doc.doc_id, self.target.doc_id)
