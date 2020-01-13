import unittest
from pychembldb import chembldb, UsanStem


class UsanStemTest(unittest.TestCase):
     def setUp(self):
         self.target = chembldb.query(UsanStem).filter_by(stem="-denoson").first()

     def test_stem(self):
         self.assertEqual(self.target.stem, "-denoson")

     def test_stem_class(self):
         self.assertEqual(self.target.stem_class, "Suffix")

     def test_annotation(self):
         self.assertEqual(self.target.annotation, "adenosine A receptor agonists")

     def test_major_class(self):
         self.assertEqual(self.target.major_class, "GPCR")

     def test_who_extra(self):
         self.assertEqual(self.target.who_extra, 0)
