import unittest
from pychembldb import chembldb, Target


class TargtTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Target).get(10)

    def test_target_type(self):
        self.assertEqual(self.target.target_type, "PROTEIN")

    def test_db_source(self):
        self.assertEqual(self.target.db_source, "SWISS-PROT")

    def test_description(self):
        self.assertEqual(self.target.description, "DNA-directed RNA polymerase subunit beta")

    def test_gene_names(self):
        self.assertEqual(self.target.gene_names, "rpoB; groN; nitB; rif; ron; stl; stv; tabD; JW3950")

    def test_pref_name(self):
        self.assertEqual(self.target.pref_name, "DNA-directed RNA polymerase beta chain")

    def test_synonyms(self):
        self.assertEqual(self.target.synonyms, "DNA-directed RNA polymerase subunit beta; RNA polymerase subunit beta; Transcriptase subunit beta; RNAP subunit beta")

    def test_keywords(self):
        self.assertEqual(self.target.keywords, "3D-structure; Acetylation; Complete proteome; DNA-directed RNA polymerase; Nucleotidyltransferase; Reference proteome; Transcription; Transferase")

    def test_protein_sequence(self):
        self.assertEqual(self.target.protein_sequence[:10], "MVYSYTEKKR")

    def test_protein_md5sum(self):
        self.assertEqual(self.target.protein_md5sum, "5a6db54270d33f1e4bfa723559a235e2")

    def test_tax_id(self):
        self.assertEqual(self.target.tax_id, 83333L)

    def test_organism(self):
        self.assertEqual(self.target.organism, "Escherichia coli K-12")

    def test_tissue(self):
        self.assertIsNone(self.target.tissue)

    def test_strain(self):
        self.assertIsNone(self.target.strain)

    def test_db_version(self):
        self.assertEqual(self.target.db_version, "2012_05")

    def test_cell_line(self):
        self.assertIsNone(self.target.cell_line)

    def test_protein_accession(self):
        self.assertEqual(self.target.protein_accession, "P0A8V2")

    def test_ec_number(self):
        self.assertEqual(self.target.ec_number, "2.7.7.6")

    def test_chembl_id(self):
        self.assertEqual(self.target.chembl_id, "CHEMBL1852")

    # TargetDictionary -> TagetType
    def test_target_types(self):
        self.assertEqual(self.target.type.target_desc, "Molecular Target identified")

    # TargetDictionary -> TagetClass
    def test_target_classes(self):
        self.assertEqual(len(self.target.target_classes), 1)

    # TargetDictionary -> Assay
    def test_target_assays(self):
        self.assertEqual(len(self.target.assays), 13)

    def test_target_assays_targets(self):
        self.assertEqual(len(self.target.assays[0].targets), 3)

    # todo
    # chemblid_lookup
    
