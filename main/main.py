import os
from compare import compareClass

compareTypes = compareClass("adipose_tissue.tsv")


compareTypes.compare()
print(os.getcwd())