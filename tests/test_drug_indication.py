import unittest
from pychembldb import chembldb, DrugIndication


class DrugindicationTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(DrugIndication).filter_by(mesh_heading="Diabetes Mellitus").first()

    def test_drugind_id(self):
        self.assertEqual(self.target.drugind_id, 22612)

    def test_max_phase_for_ind(self):
        self.assertEqual(self.target.max_phase_for_ind, 4)

    def test_mesh_id(self):
        self.assertEqual(self.target.mesh_id, "D003920")

    def test_mesh_heading(self):
        self.assertEqual(self.target.mesh_heading, "Diabetes Mellitus")

    def test_efo_id(self):
        self.assertEqual(self.target.efo_id, "EFO:0000400")

    def test_efo_term(self):
        self.assertEqual(self.target.efo_term, "diabetes mellitus")

    def test_refs(self):
        self.assertEqual(len(self.target.refs), 2)
