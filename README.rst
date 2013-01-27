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

