from pychembldb import *
import os
from glob import glob

# metadata
tsv_file = "metadata.tsv"
# sdf_dir
sdf_dir = "sdfs"
# activity_dir
act_dir = "activities"


def write_sdf(overwrite=False):
    if not os.path.exists(sdf_dir):
        os.mkdir(sdf_dir)

    # Confidence score == 9
    c9 = chembldb.query(ConfidenceScore).filter_by(
        description="Direct single protein target assigned"
        ).one()

    # write sdf_file -> for MMP
    for assay in chembldb.query(Assay).filter_by(confidencescore=c9)\
                                      .filter_by(assay_organism="Homo sapiens")\
                                      .filter(AssayType.assay_desc == "Binding")\
                                      .all():
        sdf_file = os.path.join(sdf_dir, "{}.sdf".format(assay.assay_id))

        # eliminate 'PubChem BioAssay data set'
        if assay.doc.title == "PubChem BioAssay data set":
            continue

        if overwrite == False:
            if os.path.exists(sdf_file):
                continue

        with open(sdf_file, "w") as f:
            for act in  assay.activities:
                if hasattr(act.compound.molecule.structure, "molfile"):
                    f.write(act.compound.molecule.structure.molfile)
                    f.write("\n> <ID>\n{}\n\n$$$$\n".format(act.compound.molecule.chembl_id))


def remove_empty_file():
    for file in glob("{}/*.sdf".format(sdf_dir)):
        if os.path.getsize(file) == 0:
            os.remove(file)
        else:
            txt = open(file).read()
            count = txt.count("$$$$")
            if count < 2:
                os.remove(file)


def write_metadata():
    # Confidence score == 9
    with open("metadata.tsv", "w") as metadatafile:
        metadatafile.write("assay_id\taccession\tjournal\n")
        for file in glob("{}/*.sdf".format(sdf_dir)):
            id = (file.split(".")[0]).split("/")[1]
            assay = chembldb.query(Assay).filter_by(assay_id=id).one()
            if len(assay.target.components) < 1:
                continue
            accession = assay.target.components[0].accession
            journal = "{}({}){}:{}-{}".format(
                assay.doc.journal,
                assay.doc.year,
                assay.doc.volume,
                assay.doc.first_page,
                assay.doc.last_page
                )
            metadatafile.write("{}\t{}\t{}\t{}\n".format(assay.assay_id,
                                                         accession,
                                                         assay.target.pref_name,
                                                         journal))


def write_activity():
    if not os.path.exists(act_dir):
        os.mkdir(act_dir)

    for file in glob("{}/*.sdf".format(sdf_dir)):
        id = (file.split(".")[0]).split("/")[1]
        act_file = os.path.join(act_dir, "{}.tsv".format(id))
        assay = chembldb.query(Assay).filter_by(assay_id=id).one()

        with open(act_file, "w") as act_file:
            act_file.write("chembl_id\ttype\tvalue\n")
            for activity in assay.activities:
                if activity.standard_value is not None:
                    act_file.write("{}\t{}\t{}\n".format(activity.compound.molecule.chembl_id,
                                                         activity.standard_type,
                                                         activity.standard_value))


def check_type():
    c9 = chembldb.query(ConfidenceScore).filter_by(
        description="Direct single protein target assigned"
        ).one()

    # write sdf_file -> for MMP
    for assay in chembldb.query(Assay).filter_by(confidencescore=c9)\
                                      .filter_by(assay_organism="Homo sapiens")\
                                      .filter(AssayType.assay_desc == "Binding")\
                                      .all():
        # eliminate 'PubChem BioAssay data set'
        if assay.doc.title == "PubChem BioAssay data set":
            continue

        r = []
        for act in  assay.activities:
            r.append(act.standard_type)
        rl = list(set(r))
        if len(rl) > 1:
            print assay.assay_id, rl


if __name__ == '__main__':
    #check_type()
    write_sdf()
    remove_empty_file()
    write_metadata()
    write_activity()
