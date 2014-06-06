import unittest
from pychembldb import chembldb, ComponentSequence


class ComponentSequenceTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ComponentSequence).get(1)

    def test_component_id(self):
        self.assertEqual(self.target.component_id, 1)

    def test_component_type(self):
        self.assertEqual(self.target.component_type, "PROTEIN")

    def test_accession(self):
        self.assertEqual(self.target.accession, "O09028")

    def test_sequence(self):
        self.assertEqual(self.target.sequence[:10], "MSYSLYLAFV")

    def test_sequence_md5sum(self):
        self.assertEqual(self.target.sequence_md5sum, "7473be17a767c25bb1d57beee67ffff7")

    def test_description(self):
        self.assertEqual(self.target.description, "Gamma-aminobutyric acid receptor subunit pi")

    def test_tax_id(self):
        self.assertEqual(self.target.tax_id, 10116L)

    def test_organism(self):
        self.assertEqual(self.target.organism, "Rattus norvegicus")

    def test_db_source(self):
        self.assertEqual(self.target.db_source, "SWISS-PROT")

    def test_db_version(self):
        self.assertEqual(self.target.db_version, "2014_01")
