from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pychembldb',
      version=version,
      description="ChEMBLdb interface for Python",
      long_description="""\
ChEMBLdb interface for Python""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='chemoinformatics cheminformatics',
      author='Ohkawa Kazufumi',
      author_email='kerolinq@gmail.com',
      url='http://github.com/kzfm/pychembldb',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
