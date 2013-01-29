============
 pychembldb
============

`pychembldb` is a Python interface for ChEMBLdb

Requirements
------------
* Python 2.7 or later (not support 3.x)
* MySQL-python >= 1.2.4
* SQLAlchemy >= 0.8.0b2


Setup
-----

Install
~~~~~~~

::

    git clone https://github.com/kzfm/pychembldb.git
    cd pychembldb
    sudo python setup.py install

Setting up engine_url
~~~~~~~~~~~~~~~~~~~~~

if you change engine_url, you should set CHEMBL_URI environment variable (default:mysql://root@localhost/chembl_14)

Basic Usage
-----------

::

    from pychembldb import *
    for target in chembldb.query(Target).filter_by(pref_name="Tyrosine-protein kinase ABL"):
        for assay in target.assays:
            for activity in assay.activities:
                print activity.published_value, activity.molecule.structure.standard_inchi_key

Examples
--------

::

    from pychembldb import *
    for target in chembldb.query(Target).filter_by(pref_name="Tyrosine-protein kinase ABL"):
        for assay in target.assays:
            for activity in assay.activities:
                print activity.published_value, activity.molecule.structure.standard_inchi_key

::

    for journal in chembldb.query(Doc).filter_by(doi="10.1016/S0960-894X(01)80693-4"):
        for assay in journal.assays:
            for activity in assay.activities:
                print activity.published_value, activity.molecule.structure.standard_inchi_key

::

    chembldb.query(MoleculeSynonym).filter_by(synonyms="Gleevec").first().molecule.structure.canonical_smiles
    # 'CN1CCN(Cc2ccc(cc2)C(=O)Nc3ccc(C)c(Nc4nccc(n4)c5cccnc5)c3)CC1'

History
-------

0.1.1 (2013-01-29)
~~~~~~~~~~~~~~~~~~
* Several bug fixes
* Add synonyms relation

0.1 (2013-01-29)
~~~~~~~~~~~~~~~~~~
* first release
