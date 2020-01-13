import unittest
from pychembldb import chembldb, CompoundProperty, MoleculeSynonym, Molecule
from decimal import Decimal


class MoleculeTest(unittest.TestCase):
    def setUp(self):
        self.mol = chembldb.query(MoleculeSynonym).filter_by(synonyms="Gleevec").first().molecule

    def test_molregno(self):
        self.assertEqual(self.mol.molregno, 88797)

    def test_pref_name(self):
        self.assertEqual(self.mol.pref_name, "IMATINIB")

    def test_chembl_id(self):
        self.assertEqual(self.mol.chembl_id, "CHEMBL941")

    def test_max_phase(self):
        self.assertEqual(self.mol.max_phase, 4)

    def test_therapeutic_flag(self):
        self.assertEqual(self.mol.therapeutic_flag, 1)

    def test_dosed_ingredient(self):
        self.assertEqual(self.mol.dosed_ingredient, 1)

    def test_structure_type(self):
        self.assertEqual(self.mol.structure_type, "MOL")

    def test_chebi_par_id(self):
        self.assertEqual(self.mol.chebi_par_id, 45783)

    def test_molecule_type(self):
        self.assertEqual(self.mol.molecule_type, "Small molecule")

    def test_first_approval(self):
        self.assertEqual(self.mol.first_approval, 2001)

    def test_oral(self):
        self.assertEqual(self.mol.oral, 1)

    def test_parenteral(self):
        self.assertEqual(self.mol.parenteral, 0)

    def test_topical(self):
        self.assertEqual(self.mol.topical, 0)

    def test_black_box_warning(self):
        self.assertEqual(self.mol.black_box_warning, 0)

    def test_natural_product(self):
        self.assertEqual(self.mol.natural_product, 0)

    def test_prodrug(self):
        self.assertEqual(self.mol.prodrug, 0)

    def test_inorganic_flag(self):
        self.assertEqual(self.mol.inorganic_flag, 0)

    def test_usan_year(self):
        self.assertIsNone(self.mol.usan_year)

    def test_availability_type(self):
        self.assertEqual(self.mol.availability_type, 1)

    def test_usan_stem(self):
        self.assertEqual(self.mol.usan_stem, "-tinib")

    def test_polymer_flag(self):
        self.assertEqual(self.mol.polymer_flag, 0)

    def test_usan_substem(self):
        self.assertEqual(self.mol.usan_substem, "-tinib")

    def test_usan_stem_definition(self):
        self.assertEqual(self.mol.usan_stem_definition, "tyrosine kinase inhibitors")

    def test_indication_class(self):
        self.assertIsNone(self.mol.indication_class)

    def test_withdrawn_flag(self):
        self.assertEqual(self.mol.withdrawn_flag, 0)

    def test_withdrawn_year(self):
        self.assertIsNone(self.mol.withdrawn_year)

    def test_withdrawn_country(self):
        self.assertIsNone(self.mol.withdrawn_country)

    def test_withdrawn_reason(self):
        self.assertIsNone(self.mol.withdrawn_reason)

    def test_withdrawn_class(self):
        self.assertIsNone(self.mol.withdrawn_class)


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
