import pandas as pd
import os

class tissueBase:
    def __init__(self, tissueType):
        self.tissueTypeFile = tissueType
        self.data = pd.read_csv(os.path.join('C:/~/Documents/Comp Bio 2022-23/CompBioDirectedStudy/TissueFiles/', self.tissueTypeFile), sep='\t', header=0,)
    """inputColumns accepts an array of columns found in TissueTypes."""
    def returnColumnData(self, inputColumns):
        return self.data.get(columns=inputColumns, default="NA")
    def returnAllData(self):
        return self.data
    def popColumns(self, inputColumns):
        self.data.droplevel(inputColumns)