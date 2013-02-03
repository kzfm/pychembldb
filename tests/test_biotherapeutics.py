import unittest
from pychembldb import chembldb, Biotherapeutics


class BiotherapeuticsTest(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Biotherapeutics).first()

    def test_molregno(self):
        self.assertEqual(self.target.molregno, 112560L)

    def test_description(self):
        self.assertEqual(self.target.description, "Progonadoliberin I precursor")
