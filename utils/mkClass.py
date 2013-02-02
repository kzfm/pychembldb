from singular import singularize
from sqlalchemy import create_engine, MetaData
db = create_engine('mysql://root@localhost/chembl_15')
metadata = MetaData(bind=db, reflect=True)

for table in  metadata.tables.keys():
    classname = "".join([singularize(n).capitalize() for n in table.split('_') if n not in ['dictionary', 'lookup']])
    print """class {}(Base):
    __table__ = Table('{}', metadata, autoload=True)

""".format(classname, table)
