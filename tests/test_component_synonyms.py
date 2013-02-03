import unittest
from pychembldb import chembldb, ComponentSynonym


class ComponentSynonymTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ComponentSynonym).first()

    def test_compsyn_id(self):
        self.assertEqual(self.target.compsyn_id, 129599L)

    def test_component_id(self):
        self.assertEqual(self.target.component_id, 1)

    def test_component_synonym(self):
        self.assertEqual(self.target.component_synonym, "GABA receptor pi subunit")

    def test_syn_type(self):
        self.assertEqual(self.target.syn_type, "MANUAL")
