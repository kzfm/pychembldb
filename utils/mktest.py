from singular import singularize
from sqlalchemy import create_engine, MetaData
import sys
db = create_engine('mysql://root@localhost/chembl_15')
metadata = MetaData(bind=db)
metadata.reflect()

tablename = sys.argv[1]
classname = "".join([singularize(n).capitalize() for n in tablename.split('_') if n not in ['dictionary', 'lookup']])
testname = classname + 'Test'
table = metadata.tables[tablename]

print """import unittest
from pychembldb import chembldb, {}


class {}(unittest.TestCase):
    def setUp(self):
        self.target = chembldb.query(Target).get(1)
""".format(classname, testname)

for c in table.columns:
    print """    def test_{}(self):
        self.assertEqual(self.target.{}, "")
""".format(c.name, c.name)
