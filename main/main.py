import os
from compare import compareClass
from getGene import getGeneClass

compareTypes = compareClass("ovaryES.tsv")
grabTool = getGeneClass()

matchingIDs = compareTypes.compare()
seqDF = grabTool.getSeqEnsembl(matchingIDs)

