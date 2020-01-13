import unittest
from pychembldb import chembldb, Doc


class DocTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Doc).filter_by(pubmed_id=14695833).first()

    def test_doc_id(self):
        self.assertEqual(self.target.doc_id, 10)

    def test_journal(self):
        self.assertEqual(self.target.journal, "J. Med. Chem.")

    def test_year(self):
        self.assertEqual(self.target.year, 2004)

    def test_volume(self):
        self.assertEqual(self.target.volume, "47")

    def test_issue(self):
        self.assertEqual(self.target.issue, "1")

    def test_first_page(self):
        self.assertEqual(self.target.first_page, "196")

    def test_last_page(self):
        self.assertEqual(self.target.last_page, "209")

    def test_pubmed_id(self):
        self.assertEqual(self.target.pubmed_id, 14695833)

    def test_doi(self):
        self.assertEqual(self.target.doi, "10.1021/jm0301888")

    def test_chembl_id(self):
        self.assertEqual(self.target.chembl_id, "CHEMBL1148467")

    def test_title(self):
        self.assertEqual(self.target.title[:20], "Benzoxazinones as PP")

    def test_doc_type(self):
        self.assertEqual(self.target.doc_type, "PUBLICATION")

    def test_authors(self):
        self.assertEqual(self.target.authors, "Rybczynski PJ, Zeck RE, Dudash J, Combs DW, Burris TP, Yang M, Osborne MC, Chen X, Demarest KT.")

    def test_abstract(self):
        self.assertEqual(self.target.abstract[:10], "A series o")

    def test_patent_id(self):
        self.assertIsNone(self.target.patent_id)

    def test_ridx(self):
        self.assertEqual(self.target.ridx, "CLD0")

    def test_src_id(self):
        self.assertEqual(self.target.src_id, 1)


    # doc-assay
    def test_doc_assays(self):
        self.assertEqual(len(self.target.assays), 5)

    def test_doc_assays_doc(self):
        self.assertEqual(self.target.assays[0].doc.doc_id, self.target.doc_id)

    # doc-compound_records
    def test_doc_compound_records(self):
        self.assertEqual(len(self.target.compounds), 54)

    def test_doc_compound_records_backref(self):
        self.assertEqual(self.target.compounds[0].doc.doc_id, self.target.doc_id)
