from setuptools import setup, find_packages
import sys, os

version = '0.4.1'

long_description = open("README.rst").read()

setup(name='pychembldb',
      version=version,
      description="ChEMBLdb interface for Python",
      long_description=long_description,
      long_description_content_type="text/x-rst",
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
      ])
