import unittest
from pychembldb import chembldb, Molecule


class MoleculeTest(unittest.TestCase):
    def setUp(self):
        self.mol = chembldb.query(Molecule).first()

    def test_molregno(self):
        self.assertEqual(self.mol.molregno, 1)

    def test_pref_name(self):
        self.assertIsNone(self.mol.pref_name)

    def test_chembl_id(self):
        self.assertEqual(self.mol.chembl_id, "CHEMBL6329")

    def test_max_phase(self):
        self.assertEqual(self.mol.max_phase, 0)

    def test_therapeutic_flag(self):
        self.assertEqual(self.mol.therapeutic_flag, 0)

    def test_dosed_ingredient(self):
        self.assertEqual(self.mol.dosed_ingredient, 0)

    def test_structure_type(self):
        self.assertEqual(self.mol.structure_type, "MOL")

    def test_chebi_id(self):
        self.assertEqual(self.mol.chebi_id, 100001L)

    def test_chebi_par_id(self):
        self.assertIsNone(self.mol.chebi_par_id)

    def test_molecule_type(self):
        self.assertEqual(self.mol.molecule_type, "Small molecule")

    def test_first_approval(self):
        self.assertIsNone(self.mol.first_approval)

    def test_oral(self):
        self.assertEqual(self.mol.oral, 0)

    def test_parenteral(self):
        self.assertEqual(self.mol.parenteral, 0)

    def test_topical(self):
        self.assertEqual(self.mol.topical, 0)

    def test_black_box_warning(self):
        self.assertEqual(self.mol.black_box_warning, 0)

    def test_natural_product(self):
        self.assertEqual(self.mol.natural_product, -1)

    def test_prodrug(self):
        self.assertEqual(self.mol.prodrug, -1)

    # mol-compound_records
    def test_compound_backref(self):
        self.assertEqual(self.mol.compound.molregno, self.mol.molregno)

    # mol-compound_structure
    def test_structure_backref(self):
        self.assertEqual(self.mol.structure.molregno, self.mol.molregno)

    # mol-compound_properties
    def test_property_backref(self):
        self.assertEqual(self.mol.property.molregno, self.mol.molregno)

    # mol-hierarchy
    #def test_hierarchy(self):
    #    self.assertEqual(self.mol.hierarchy.molregno, self.mol.molregno)

    # mol-compound_properties
    def test_biotherapeutics(self):
        self.assertIsNone(self.mol.biotherapeutics)

    ### Todo (relation)
    # chembl_id, protein_therapy


class MoleculeSynonymTest(unittest.TestCase):
    def setUp(self):
        self.mol = chembldb.query(Molecule).filter_by(chembl_id="CHEMBL941").first()

    # mol-synonyms
    def test_synonyms(self):
        self.assertEqual(len(self.mol.synonyms), 7)

    def test_synonyms_backref(self):
        self.assertEqual(self.mol.synonyms[0].molregno, self.mol.molregno)
