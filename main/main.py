import os
from compare import compareClass
from getGene import getGeneClass
from siRNARuleDesign import siRNADesign

compareTypes = compareClass("ovary.tsv", True)
grabTool = getGeneClass()


matchingIDs = compareTypes.compare()
print(grabTool.getSeqEnsembl(matchingIDs))


