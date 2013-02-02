from sqlalchemy import create_engine, MetaData
import sys
db = create_engine('mysql://root@localhost/chembl_14')
metadata = MetaData(bind=db, reflect=True)

table = metadata.tables[sys.argv[1]]

for c in table.columns:
    print """    def test_{}(self):
        self.assertEqual(self.target.{}, "")
""".format(c.name, c.name)
