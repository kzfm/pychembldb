from pychembldb import *
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast import NCBIXML
from StringIO import StringIO
import subprocess

def format_seq(s):
    l = len(s)
    n = 70
    return "\n".join([s[i:i+n] for i in range(0, l, n)])


def make_db():
    with open("chembl.fasta", "w") as f:
        for t in chembldb.query(Target):
            if len(t.components) > 0:
                f.write(">lcl|{}| {}\n{}\n".format(t.chembl_id,
                                               t.pref_name,
                                               format_seq(t.components[0].sequence)))

if __name__ == '__main__':
    make_db()
    subprocess.call(["makeblastdb", "-in", "chembl.fasta", "-dbtype", "prot", "-hash_index", "-parse_seqids"])
    blastp_client = NcbiblastpCommandline(query="query.aa",
                                          db="chembl.fasta",
                                          evalue=1e-10,
                                          outfmt=5)
    stdout, stderr = blastp_client()
    r = NCBIXML.read(StringIO(stdout))
    for desc in r.descriptions:
        print desc.title, desc.e
