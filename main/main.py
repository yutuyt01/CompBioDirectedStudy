import os
from compare import compareClass
from getGene import getGeneClass

compareTypes = compareClass("ovary.tsv", True)
grabTool = getGeneClass()

matchingIDs = compareTypes.compare()
print(grabTool.getSeqEnsembl(matchingIDs))

