============
 pychembldb
============

`pychembldb` is a Python interface for ChEMBLdb

Requirements
------------
* Python 2.7 or later (not support 3.x)
* MySQL-python >= 1.2.4 or psycopg2 >= 2.5.1
* SQLAlchemy >= 0.8.0b2

ChEMBLdb
~~~~~~~~

* pychembldb-0.1.x support chembl_14
* pychembldb-0.2.x support chembl_15 and chembl_16
* pychembldb-0.3.x support chembl_17,18,19

Setup
-----

Install
~~~~~~~

::

    pip install pychembldb

or install from github

::

    git clone https://github.com/kzfm/pychembldb.git
    cd pychembldb
    sudo python setup.py install

Setting up engine_url
~~~~~~~~~~~~~~~~~~~~~

if you change engine_url, you should set CHEMBL_URI environment variable (default:mysql://root@localhost/chembl_18)

ex) PostgreSQL

::

    export CHEMBL_URI="postgresql+psycopg2://localhost/chembl_18"

    or

    export CHEMBL_URI="postgresql+psycopg2://USER:PASSWORD@localhost/chembl_18"    


Basic Usage
-----------

::

    from pychembldb import *
    for target in chembldb.query(Target).filter_by(pref_name="Tyrosine-protein kinase ABL"):
        for assay in target.assays:
            for activity in assay.activities:
                print activity.published_value, activity.compound.molecule.structure.standard_inchi_key

Examples
--------

filter activities and compound structures by Target(Protein).

::

    from pychembldb import *
    for target in chembldb.query(Target).filter_by(pref_name="Tyrosine-protein kinase ABL"):
        for assay in target.assays:
            for activity in assay.activities:
                print activity.published_value, activity.compound.molecule.structure.standard_inchi_key

Search activities and compound structures from Journal-ID(doi).

::

    for journal in chembldb.query(Doc).filter_by(doi="10.1016/S0960-894X(01)80693-4"):
        for assay in journal.assays:
            for activity in assay.activities:
                print activity.published_value, activity.compound.molecule.structure.standard_inchi_key

Get SMILES from Molecule synonyms.

::

    chembldb.query(MoleculeSynonym).filter_by(synonyms="Gleevec").first().molecule.structure.canonical_smiles
    # 'CN1CCN(Cc2ccc(cc2)C(=O)Nc3ccc(C)c(Nc4nccc(n4)c5cccnc5)c3)CC1'

Count the number of MedChem Friendly Compounds.

::

    chembldb.query(CompoundProperty).filter_by(med_chem_friendly='Y').count()

See also.

* http://docs.sqlalchemy.org/en/rel_0_8/orm/tutorial.html
* ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_18_erd.png

History
-------

0.3.6 (2014-09-02)
~~~~~~~~~~~~~~~~~~
* Support ChEMBLdb 19

0.3.4 (2014-06-07)
~~~~~~~~~~~~~~~~~~
* Update document
* Support ATC Classifications

0.3.3 (2014-06-06)
~~~~~~~~~~~~~~~~~~
* Support ChEMBLdb 18

0.3.2 (2014-01-13)
~~~~~~~~~~~~~~~~~~
* Fix bug

0.3.1 (2013-12-17)
~~~~~~~~~~~~~~~~~~
* Support ChEMBLdb 17

0.2.1 (2013-06-15)
~~~~~~~~~~~~~~~~~~
* Support ChEMBLdb 16

0.2.0 (2013-02-03)
~~~~~~~~~~~~~~~~~~
* Support ChEMBLdb 15

0.1.1 (2013-01-29)
~~~~~~~~~~~~~~~~~~
* Several bug fixes
* Add synonyms relation

0.1 (2013-01-29)
~~~~~~~~~~~~~~~~~~
* first release
