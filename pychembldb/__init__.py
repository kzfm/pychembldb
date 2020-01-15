import os
from sqlalchemy import *
from sqlalchemy.orm import create_session, relationship
from sqlalchemy.ext.declarative import declarative_base

uri = 'mysql://root@localhost/chembl_25'
if 'CHEMBL_URI' in os.environ:
    uri = os.environ['CHEMBL_URI']

Base = declarative_base()
engine = create_engine(uri)
metadata = MetaData(bind=engine)


### Target
class CellDictionary(Base):
    __table__ = Table('cell_dictionary', metadata, autoload=True)


class TargetDictionary(Base):
    __table__ = Table('target_dictionary', metadata, autoload=True)
    components = relationship('ComponentSequence', secondary=Table('target_components', metadata, autoload=True), backref='target')
    assays = relationship('Assay', backref='target')
    binding_sites = relationship('BindingSite', backref='target')
    #predicted_binding_domains = relationship('PredictedBindingDomain', backref='target')

class TargetType(Base):
    __table__ = Table('target_type', metadata, autoload=True)
    targets = relationship('TargetDictionary', backref='type')


class OrganismClass(Base):
    __table__ = Table('organism_class', metadata, autoload=True)
    #targets = relationship('TargetDictionary', backref='organism')


class ComponentSequence(Base):
    __table__ = Table('component_sequences', metadata, autoload=True)
    classes = relationship('ProteinClassification', secondary=Table('component_class', metadata, autoload=True), backref='component')
    synonyms = relationship('ComponentSynonym', backref='component')
    componentdomains = relationship('ComponentDomain', backref='component')
    sitecomponents = relationship('SiteComponent', backref='component')
    targets = relationship('TargetDictionary', secondary=Table('target_components', metadata, autoload=True), backref='component')
    domains = relationship('Domain', secondary=Table('component_domains', metadata, autoload=True), backref='component')
    binding_sites = relationship('BindingSite', secondary=Table('site_components', metadata, autoload=True), backref='component')


class ProteinClassification(Base):
    __table__ = Table('protein_classification', metadata, autoload=True)
    components = relationship('ComponentSequence', secondary=Table('component_class', metadata, autoload=True), backref='family')
    synonyms = relationship('ProteinClassSynonym', backref='class')


class ProteinClassSynonym(Base):
    __table__ = Table('protein_class_synonyms', metadata, autoload=True)


class ComponentSynonym(Base):
    __table__ = Table('component_synonyms', metadata, autoload=True)


class TissueDictionary(Base):
    __table__ = Table('tissue_dictionary', metadata, autoload=True)
    assays = relationship('Assay', backref='tissue')


class VariantSequence(Base):
    __table__ = Table('variant_sequences', metadata, autoload=True)
    assays = relationship('Assay', backref='variant_sequence')


class GOClassification(Base):
    __table__ = Table('go_classification', metadata, autoload=True)
    components = relationship('ComponentSequence', secondary=Table('component_go', metadata, autoload=True), backref='gos')


class ProteinFamilyClassification(Base):
    __table__ = Table('protein_family_classification', metadata, autoload=True)


### Binding-Sites
class ComponentDomain(Base):
    __table__ = Table('component_domains', metadata, autoload=True)


class BindingSite(Base):
    __table__ = Table('binding_sites', metadata, autoload=True)
    sitecomponents = relationship('SiteComponent', backref='binding_site')
    predicted_binding_domains = relationship('PredictedBindingDomain', backref='binding_site')
    domains = relationship('Domain', secondary=Table('site_components', metadata, autoload=True), backref='binding_sites')
    components = relationship('ComponentSequence', secondary=Table('site_components', metadata, autoload=True), backref='bindingsites')


class Domain(Base):
    __table__ = Table('domains', metadata, autoload=True)
    componentdomains = relationship('ComponentDomain', backref='domain')
    sites = relationship('SiteComponent', backref='domain')
    components = relationship('ComponentSequence', secondary=Table('component_domains', metadata, autoload=True), backref='domain')


class SiteComponent(Base):
    __table__ = Table('site_components', metadata, autoload=True)


### Mechanism
class PredictedBindingDomain(Base):
    __table__ = Table('predicted_binding_domains', metadata, autoload=True)


class LigandEff(Base):
    __table__ = Table('ligand_eff', metadata, autoload=True)


### Drug Data
class Product(Base):
    __table__ = Table('products', metadata, autoload=True)
    formulations = relationship('Formulation', backref='product')
    molecules = relationship('MoleculeDictionary', secondary=Table('formulations', metadata, autoload=True), backref='mol_products')


class DefinedDailyDose(Base):
    __table__ = Table('defined_daily_dose', metadata, autoload=True)


class Formulation(Base):
    __table__ = Table('formulations', metadata, autoload=True)


class AtcClassification(Base):
    __table__ = Table('atc_classification', metadata, autoload=True)
    dose = relationship('DefinedDailyDose', uselist=False, backref='atc')
    molecules = relationship('MoleculeDictionary', secondary=Table('molecule_atc_classification', metadata, autoload=True), backref='atcs')
    defined_daily_dose = relationship('DefinedDailyDose', uselist=False, backref='atc_classification')


class UsanStem(Base):
    __table__ = Table('usan_stems', metadata, autoload=True)


class HracClassification(Base):
    __table__ = Table('hrac_classification', metadata, autoload=True)


class IracClassification(Base):
    __table__ = Table('irac_classification', metadata, autoload=True)


class FracClassification(Base):
    __table__ = Table('frac_classification', metadata, autoload=True)


class PatentUseCode(Base):
    __table__ = Table('patent_use_codes', metadata, autoload=True)
    products = relationship('Product', secondary=Table('product_patents', metadata, autoload=True), backref='codes')
    patents = relationship('ProductPatent', backref='code')

class ProductPatent(Base):
    __table__ = Table('product_patents', metadata, autoload=True)

### Mechanism/Indication

class DrugIndication(Base):
    __table__ = Table('drug_indication', metadata, autoload=True)
    refs = relationship('IndicationRefs', backref='indication')


class IndicationRefs(Base):
    __table__ = Table('indication_refs', metadata, autoload=True)


class DrugMechanism(Base):
    __table__ = Table('drug_mechanism', metadata, autoload=True)
    refs = relationship('MechanismRefs', backref='mechanism')


class ActionType(Base):
    __table__ = Table('action_type', metadata, autoload=True)
    mechanisms = relationship('DrugMechanism', backref='actiontype')


class MechanismRefs(Base):
    __table__ = Table('mechanism_refs', metadata, autoload=True)

### Metbolism

class Metabolism(Base):
    __table__ = Table('metabolism', metadata, autoload=True)
    refs = relationship('MetabolismRefs', backref='metabolism')


class MetabolismRefs(Base):
    __table__ = Table('metabolism_refs', metadata, autoload=True)


### Compounds
class CompoundProperty(Base):
    __table__ = Table('compound_properties', metadata, autoload=True)


class CompoundStructure(Base):
    __table__ = Table('compound_structures', metadata, autoload=True)


class MoleculeHierarchy(Base):
    __table__ = Table('molecule_hierarchy', metadata, autoload=True)


class ResearchCompany(Base):
    __table__ = Table('research_companies', metadata, autoload=True)


class MoleculeDictionary(Base):
    __table__ = Table('molecule_dictionary', metadata, autoload=True)
    compound = relationship('CompoundRecord', uselist=False, backref='molecule')
    structure = relationship('CompoundStructure', uselist=False, backref='molecule')
    property = relationship('CompoundProperty', uselist=False, backref='molecule')
    formulations = relationship('Formulation', backref='molecule')
    synonyms = relationship('MoleculeSynonym', backref='molecule')
    biotherapeutics = relationship('Biotherapeutics', uselist=False, backref='molecule')
    #hierarchy = relationship('MoleculeHierarchy', uselist=False, backref='molecule')
    atc_classifications = relationship('AtcClassification', secondary=Table('molecule_atc_classification', metadata, autoload=True), backref='atc_molecules')
    products = relationship('MoleculeDictionary', secondary=Table('formulations', metadata, autoload=True), backref='product_molecules')


class MoleculeSynonym(Base):
    __table__ = Table('molecule_synonyms', metadata, autoload=True)
    research_stem = relationship('ResearchStem', backref='molecule_synonym')


class ResearchStem(Base):
    __table__ = Table('research_stem', metadata, autoload=True)
    companies = relationship('ResearchCompany', backref='stem')
    synonyms = relationship('MoleculeSynonym', backref='stem')


class CompoundRecord(Base):
    __table__ = Table('compound_records', metadata, autoload=True)
    activities = relationship('Activity', backref='compound')
    formulations = relationship('Formulation', backref='compound')


class Biotherapeutics(Base):
    __table__ = Table('biotherapeutics', metadata, autoload=True)
    components = relationship('BioComponentSequence', secondary=Table('biotherapeutic_components', metadata, autoload=True), backref='biotherapeutics')


class BioComponentSequence(Base):
    __table__ = Table('bio_component_sequences', metadata, autoload=True)
    therapeutics = relationship('Biotherapeutics', secondary=Table('biotherapeutic_components', metadata, autoload=True), backref='component')


class StructuralAlert(Base):
    __table__ = Table('structural_alerts', metadata, autoload=True)
    molecules = relationship('MoleculeDictionary', secondary=Table('compound_structural_alerts', metadata, autoload=True), backref='alerts')


class StructuralAlertSet(Base):
    __table__ = Table('structural_alert_sets', metadata, autoload=True)
    alerts = relationship('StructuralAlert', backref='alert_set')  

### Exp Data
class ActivityStdLookup(Base):
    __table__ = Table('activity_stds_lookup', metadata, autoload=True)


class DataValidityLookup(Base):
    __table__ = Table('data_validity_lookup', metadata, autoload=True)
    activities = relationship('Activity', backref='datavalidity')


class AssayType(Base):
    __table__ = Table('assay_type', metadata, autoload=True)
    assays = relationship('Assay', backref='type')


class CurationLookup(Base):
    __table__ = Table('curation_lookup', metadata, autoload=True)
    assays = relationship('Assay', backref='curation')


class RelationshipType(Base):
    __table__ = Table('relationship_type', metadata, autoload=True)
    assays = relationship('Assay', backref='relationship')


class ConfidenceScoreLookup(Base):
    __table__ = Table('confidence_score_lookup', metadata, autoload=True)
    assays = relationship('Assay', backref='confidencescore')


class Activity(Base):
    __table__ = Table('activities', metadata, autoload=True)
    predicted_binding_domain = relationship('PredictedBindingDomain', uselist=False, backref='activity')
    le = relationship('LigandEff', uselist=False, backref='activity')
    properties = relationship('ActivityProperty', uselist=False, backref='activity')

class Assay(Base):
    __table__ = Table('assays', metadata, autoload=True)
    activities = relationship(Activity, backref='assay')


class AssayClassification(Base):
    __table__ = Table('assay_classification', metadata, autoload=True)
    assays = relationship(Assay, secondary=Table('assay_class_map', metadata, autoload=True), backref='classifications')


class BioassayOntology(Base):
    __table__ = Table('bioassay_ontology', metadata, autoload=True)


class ActivityProperty(Base):
    __table__ = Table('activity_properties', metadata, autoload=True)


class ActivitySupp(Base):
    __table__ = Table('activity_supp', metadata, autoload=True)


class AssayParameter(Base):
    __table__ = Table('assay_parameters', metadata, autoload=True)


### Doc
class Doc(Base):
    __table__ = Table('docs', metadata, autoload=True)
    assays = relationship('Assay', backref='doc')
    compounds = relationship('CompoundRecord', backref='doc')


class Source(Base):
    __table__ = Table('source', metadata, autoload=True)
    assays = relationship('Assay', backref='source')
    compounds = relationship('CompoundRecord', backref='source')


### Etc
class ChemblIdLookup(Base):
    __table__ = Table('chembl_id_lookup', metadata, autoload=True)


class Version(Base):
    __table__ = Table('version', metadata, autoload=True)


### Session
chembldb = create_session(bind=engine)


### synonyms
Cell = CellDictionary
Target = TargetDictionary
Molecule = MoleculeDictionary
Tissue = TissueDictionary
Curation = CurationLookup
DataValidity = DataValidityLookup
ActivityStd = ActivityStdLookup
ConfidenceScore = ConfidenceScoreLookup
ChemblId = ChemblIdLookup
Indication = DrugIndication
