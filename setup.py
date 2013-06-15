from setuptools import setup, find_packages
import sys, os

version = '0.2.1'

setup(name='pychembldb',
      version=version,
      description="ChEMBLdb interface for Python",
      long_description="""\
============
 pychembldb
============

`pychembldb` is a Python interface for ChEMBLdb

Requirements
------------
* Python 2.7 or later (not support 3.x)
* MySQL-python >= 1.2.4
* SQLAlchemy >= 0.8.0b2

ChEMBLdb
~~~~~~~~

* pychembldb-0.1.x support chembl_14
* pychembldb-0.2.x support chembl_15 or later

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

if you change engine_url, you should set CHEMBL_URI environment variable (default:mysql://root@localhost/chembl_16)

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
* ftp://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/latest/chembl_14_erd.png

History
-------

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

""",
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python'
        ],
      keywords='chemoinformatics cheminformatics',
      author='Ohkawa Kazufumi',
      author_email='kerolinq@gmail.com',
      url='http://github.com/kzfm/pychembldb',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "SQLAlchemy >= 0.8.0b2"
      ]
      )
