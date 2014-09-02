import unittest
from pychembldb import chembldb, ComponentSynonym


class ComponentSynonymTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(ComponentSynonym).filter_by(component_id=7868).first()

    def test_compsyn_id(self):
        self.assertEqual(self.target.compsyn_id, 397225)

    def test_component_id(self):
        self.assertEqual(self.target.component_id, 7868)

    def test_component_synonym(self):
        self.assertEqual(self.target.component_synonym, "gB")

    def test_syn_type(self):
        self.assertEqual(self.target.syn_type, "GENE_SYMBOL")
