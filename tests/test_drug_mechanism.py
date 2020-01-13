import unittest
from pychembldb import chembldb, DrugMechanism


class DrugMechanismTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(DrugMechanism).first()

    def test_mec_id(self):
        self.assertEqual(self.target.mec_id, 13)

    def test_mechanism_of_action(self):
        self.assertEqual(self.target.mechanism_of_action, "Carbonic anhydrase VII inhibitor")

    def test_direct_interaction(self):
        self.assertEqual(self.target.direct_interaction, 1)

    def test_molecular_mechanism(self):
        self.assertEqual(self.target.molecular_mechanism, 1)

    def test_disease_efficacy(self):
        self.assertEqual(self.target.disease_efficacy, 1)

    def test_mechanism_comment(self):
        self.assertEqual(self.target.mechanism_comment, None)

    def test_selectivity_comment(self):
        self.assertEqual(self.target.selectivity_comment, None)

    def test_binding_site_comment(self):
        self.assertEqual(self.target.binding_site_comment, None)

