import unittest
from pychembldb import chembldb, Target


class TargetTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Target).filter_by(chembl_id="CHEMBL2074").first()

    def test_tid(self):
        self.assertEqual(self.target.tid, 1)

    def test_target_type(self):
        self.assertEqual(self.target.target_type, "SINGLE PROTEIN")

    def test_pref_name(self):
        self.assertEqual(self.target.pref_name, "Maltase-glucoamylase")

    def test_tax_id(self):
        self.assertEqual(self.target.tax_id, 9606)

    def test_organism(self):
        self.assertEqual(self.target.organism, "Homo sapiens")

    def test_chembl_id(self):
        self.assertEqual(self.target.chembl_id, "CHEMBL2074")

    def test_species_group_flag(self):
        self.assertEqual(self.target.species_group_flag, 0)

    # TargetDictionary -> TagetType
    def test_target_types(self):
        self.assertEqual(self.target.type.target_desc, "Target is a single protein chain")

    # TargetDictionary -> Assay
    def test_target_assays(self):
        self.assertEqual(len(self.target.assays), 42    )

    def test_target_assays_targets(self):
        self.assertEqual(self.target.assays[0].target.tid, 1)

    # TargetDictionary -> BindingSites
    def test_binding_sites(self):
        self.assertEqual(len(self.target.binding_sites), 0)

    # TargetDictionary -> Molecules
    def test_molecules(self):
        self.assertEqual(len(self.target.molecules), 2)

    # TargetDictionary -> Compounds
    def test_compouds(self):
        self.assertEqual(len(self.target.compounds), 2)