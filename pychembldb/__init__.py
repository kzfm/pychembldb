import os
from sqlalchemy import *
from sqlalchemy.orm import create_session, relationship
from sqlalchemy.ext.declarative import declarative_base

uri = 'mysql://root@localhost/chembl_14'
if 'CHEMBL_URI' in os.environ:
    uri = os.environ['CHEMBL_URI']

Base = declarative_base()
engine = create_engine(uri)
metadata = MetaData(bind=engine)


class Assay2Target(Base):
    __table__ = Table('assay2target', metadata, autoload=True)


class CompoundStructure(Base):
    __table__ = Table('compound_structures', metadata, autoload=True)


class CompoundProperty(Base):
    __table__ = Table('compound_properties', metadata, autoload=True)


class CompoundRecord(Base):
    __table__ = Table('compound_records', metadata, autoload=True)
    activities = relationship('Activity', backref='compound')


class TargetClass(Base):
    __table__ = Table('target_class', metadata, autoload=True)


class MoleculeSynonym(Base):
    __table__ = Table('molecule_synonyms', metadata, autoload=True)


class MoleculeHierarchy(Base):
    __table__ = Table('molecule_hierarchy', metadata, autoload=True)


class Target(Base):
    __table__ = Table('target_dictionary', metadata, autoload=True)
    target_classes = relationship("TargetClass", backref='dictinary')


class TargetType(Base):
    __table__ = Table('target_type', metadata, autoload=True)
    target_dictionaries = relationship("Target", backref='type')


class OrganismClass(Base):
    __table__ = Table('organism_class', metadata, autoload=True)


class Molecule(Base):
    __table__ = Table('molecule_dictionary', metadata, autoload=True)
    compound = relationship('CompoundRecord', uselist=False, backref='molecule')
    activities = relationship('Activity', backref='molecule')
    structure = relationship('CompoundStructure', uselist=False, backref='molecule')
    property = relationship('CompoundProperty', uselist=False, backref='molecule')
    formulation = relationship('Formulation', uselist=False, backref='molecule')
    synonyms = relationship('MoleculeSynonym', backref='molecule')
    #hierarchy = relationship('MoleculeHierarchy', uselist=False, backref='molecule')


class CurationLookup(Base):
    __table__ = Table('curation_lookup', metadata, autoload=True)


class ResearchCode(Base):
    __table__ = Table('research_codes', metadata, autoload=True)


class DefinedDailyDose(Base):
    __table__ = Table('defined_daily_dose', metadata, autoload=True)


class AtcClassification(Base):
    __table__ = Table('atc_classification', metadata, autoload=True)
    #dose = relationship('DefinedDailyDose', uselist=False, backref='atc')


class Formulation(Base):
    __table__ = Table('formulations', metadata, autoload=True)


class Product(Base):
    __table__ = Table('products', metadata, autoload=True)
    formulations = relationship(Formulation, backref='product')


class Version(Base):
    __table__ = Table('version', metadata, autoload=True)


class Activity(Base):
    __table__ = Table('activities', metadata, autoload=True)


class Assay(Base):
    __table__ = Table('assays', metadata, autoload=True)
    targets = relationship(Target, secondary=Table('assay2target', metadata, autoload=True), backref='assays')
    activities = relationship(Activity, backref='assay')


class AssayType(Base):
    __table__ = Table('assay_type', metadata, autoload=True)
    assays = relationship("Assay", backref='type')


# ArgumentError: Mapper Mapper|LigandEff|ligand_eff could not assemble any primary key columns for mapped table 'ligand_eff'
#class LigandEff(Base):
#    __table__ = Table('ligand_eff', metadata, autoload=True)


class Doc(Base):
    __table__ = Table('docs', metadata, autoload=True)
    assays = relationship("Assay", backref='doc')
    activities = relationship(Activity, backref='doc')
    compounds = relationship(CompoundRecord, backref='doc')


class Source(Base):
    __table__ = Table('source', metadata, autoload=True)
    assays = relationship("Assay", backref='source')
    #compounds = relationship(Assay, backref='compound')


class ProteinTherapeutic(Base):
    __table__ = Table('protein_therapeutics', metadata, autoload=True)


class RelationshipType(Base):
    __table__ = Table('relationship_type', metadata, autoload=True)


class ConfidenceScore(Base):
    __table__ = Table('confidence_score_lookup', metadata, autoload=True)


class ChemblIdLookup(Base):
    __table__ = Table('chembl_id_lookup', metadata, autoload=True)


chembldb = create_session(bind=engine)
