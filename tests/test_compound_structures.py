import unittest
from pychembldb import chembldb, CompoundStructure


class CompoundStructureTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(CompoundStructure).first()

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 1)

    def test_molfile(self):
        self.assertEqual(self.target.molfile[:10], "\n         ")

    def test_standard_inchi(self):
        self.assertEqual(self.target.standard_inchi, "InChI=1S/C17H12ClN3O3/c1-10-8-11(21-17(24)20-15(22)9-19-21)6-7-12(10)16(23)13-4-2-3-5-14(13)18/h2-9H,1H3,(H,20,22,24)")

    def test_standard_inchi_key(self):
        self.assertEqual(self.target.standard_inchi_key, "OWRSAHYFSSNENM-UHFFFAOYSA-N")

    def test_canonical_smiles(self):
        self.assertEqual(self.target.canonical_smiles, "Cc1cc(ccc1C(=O)c2ccccc2Cl)N3N=CC(=O)NC3=O")
