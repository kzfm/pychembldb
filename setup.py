from setuptools import setup, find_packages
import sys, os

version = '0.1'

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

History
-------

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
