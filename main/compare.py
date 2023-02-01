import parseTissueType
import os
import pandas as pd
from parseTissueType import tissueBase


class compareClass:
    def __init__(self, tissueType, elevated):
        self.tissueData = tissueBase(tissueType, False, elevated)
        print(self.tissueData.data)
        self.TFactorData = tissueBase(tissueType, True, False)
    def compare(self):
        tissueEnsembl = self.tissueData.returnColumnData("Ensembl")
        TFactorEnsembl = self.TFactorData.returnColumnData("Ensembl")
        print(tissueEnsembl)
        print(TFactorEnsembl)
        tissueAligned, TFactorAligned = tissueEnsembl.align(TFactorEnsembl, axis = 0)
        print(tissueAligned)
        print(TFactorAligned)
        aligned = []
        alignedDF = pd.Series()
        for i, v in tissueAligned.items():
            #print(v)
            if v in TFactorAligned.values:
                #print("found")
                aligned.append(v)
        alignedS = pd.Series(data=aligned)
        final = pd.concat([alignedDF, alignedS])
        print(final)
        return final

       
    def printTest(self):
        return print(self.compare)


