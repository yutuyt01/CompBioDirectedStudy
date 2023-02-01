import os
from urllib.error import HTTPError
import gget
import pandas as pd
from Bio import Entrez
from Bio import SeqIO

class getGeneClass:
    def __init__(self):
        # my personal email, tim and api key
        # TODO perhaps make an input box for user api key
        Entrez.email = "shanghaisuzhou2@gmail.com"
        Entrez.api_key = "96204496a66b47dbd039de72721fad596b08"
    def ensemblExpand(self, ids):
        pass
        #seqList = {}
        #i = 0 
        #uncomment below
        # infoDF = pd.DataFrame(gget.info(ids))
        #infoNCBIGIDs = infoDF.get("ncbi_gene_id")
        #GeneIDsSeries = pd.Series(infoNCBIGIDs)
        #GeneIDsSeries = pd.Series(['2274', '1491', '5178','150921'])
        #print(GeneIDsSeries)
        #for i, v in GeneIDsSeries.items():
    
            #searchHandle = Entrez.efetch(db="gene", id=GeneIDsSeries.items(), rettype="gene_table", retmode="text")
        
            #print(searchHandle.read())
            #searchHandle.close()
        
            
        
        #seqList = gget.seq(ids)
        #print(seqList)
        #infoDF.insert(1, "FASTA", seqList)
        #for i, v in self.ids.iterrows():
        #    seqList[i] = gget.seq(v)   
        #print(infoNCBIGIDs)
    def getSeqEnsembl(self, ids):
        gget.seq(ids, save=True)
        with open(os.path.join(os.getcwd(), "gget_seq_results.fa")) as fasta:
            #headers = []
            sequences = []
            for seq_record in SeqIO.parse(fasta, 'fasta'):
                #headers.append(seq_record.id)
                sequences.append(str(seq_record.seq))
        hs = pd.Series(ids)
        ss = pd.Series(sequences, name="FASTA Seq")
        return pd.DataFrame(dict(ID=hs, seq=ss)).set_index(['ID'])
        
            

