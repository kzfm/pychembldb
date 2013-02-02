from singular import singularize
from sqlalchemy import create_engine, MetaData
db = create_engine('mysql://root@localhost/chembl_15')
metadata = MetaData(bind=db)
metadata.reflect()

for table in  metadata.tables.keys():
    print table
