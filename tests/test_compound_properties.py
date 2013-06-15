import unittest
from pychembldb import chembldb, CompoundProperty
from decimal import Decimal


class CompoundPropertyTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(CompoundProperty).first()

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 1)

    def test_mw_freebase(self):
        self.assertEqual(self.target.mw_freebase, 341.75)

    def test_alogp(self):
        self.assertEqual(self.target.alogp, Decimal('3.34'))

    def test_hba(self):
        self.assertEqual(self.target.hba, 4)

    def test_hbd(self):
        self.assertEqual(self.target.hbd, 1)

    def test_psa(self):
        self.assertEqual(self.target.psa, Decimal('78.84'))

    def test_rtb(self):
        self.assertEqual(self.target.rtb, 3)

    def test_ro3_pass(self):
        self.assertEqual(self.target.ro3_pass, "N")

    def test_num_ro5_violations(self):
        self.assertEqual(self.target.num_ro5_violations, 0)

    def test_med_chem_friendly(self):
        self.assertEqual(self.target.med_chem_friendly, "Y")

    def test_acd_most_apka(self):
        self.assertEqual(self.target.acd_most_apka, Decimal('6.44'))

    def test_acd_most_bpka(self):
        self.assertIsNone(self.target.acd_most_bpka)

    def test_acd_logp(self):
        self.assertEqual(self.target.acd_logp, Decimal('3.19'))

    def test_acd_logd(self):
        self.assertEqual(self.target.acd_logd, Decimal('2.22'))

    def test_molecular_species(self):
        self.assertEqual(self.target.molecular_species, "ACID")

    def test_full_mwt(self):
        self.assertEqual(self.target.full_mwt, 341.75)
