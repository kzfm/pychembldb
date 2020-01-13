import unittest
from pychembldb import chembldb, CompoundProperty, MoleculeSynonym
from decimal import Decimal

class CompoundPropertyTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(MoleculeSynonym).filter_by(synonyms="Gleevec").first().molecule.property

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 88797)

    def test_mw_freebase(self):
        self.assertEqual(self.target.mw_freebase, Decimal('493.62'))

    def test_alogp(self):
        self.assertEqual(self.target.alogp, Decimal('4.59'))

    def test_hba(self):
        self.assertEqual(self.target.hba, 7)

    def test_hbd(self):
        self.assertEqual(self.target.hbd, 2)

    def test_psa(self):
        self.assertEqual(self.target.psa, Decimal('86.28'))

    def test_rtb(self):
        self.assertEqual(self.target.rtb, 7)

    def test_ro3_pass(self):
        self.assertEqual(self.target.ro3_pass, "N")

    def test_num_ro5_violations(self):
        self.assertEqual(self.target.num_ro5_violations, 0)

# deprecated?
#    def test_med_chem_friendly(self):
#        self.assertEqual(self.target.med_chem_friendly, "Y")

    def test_acd_most_apka(self):
        self.assertEqual(self.target.acd_most_apka, Decimal('13.28'))

    def test_acd_most_bpka(self):
        self.assertEqual(self.target.acd_most_bpka, Decimal('7.55'))

    def test_acd_logp(self):
        self.assertEqual(self.target.acd_logp, Decimal('2.89'))

    def test_acd_logd(self):
        self.assertEqual(self.target.acd_logd, Decimal('2.49'))

    def test_molecular_species(self):
        self.assertEqual(self.target.molecular_species, "NEUTRAL")

    def test_full_mwt(self):
        self.assertEqual(self.target.full_mwt, Decimal('493.62'))

    def test_aromatic_rings(self):
        self.assertEqual(self.target.aromatic_rings, 4)

    def test_heavy_atoms(self):
        self.assertEqual(self.target.heavy_atoms, 37)

    def test_qed_weighted(self):
        self.assertEqual(self.target.qed_weighted, Decimal('0.39'))

    def test_mw_monoisotopic(self):
        self.assertEqual(self.target.mw_monoisotopic, Decimal('493.2590'))

    def test_full_molformula(self):
        self.assertEqual(self.target.full_molformula, "C29H31N7O")

    def test_hba_lipinski(self):
        self.assertEqual(self.target.hba_lipinski, 8)

    def test_hbd_lipinski(self):
        self.assertEqual(self.target.hbd_lipinski, 2)

    def test_num_lipinski_ro5_violations(self):
        self.assertIsNone(self.target.num_lipinski_ro5_violations)

