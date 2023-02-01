import pandas as pd
import os

class tissueBase:
    def __init__(self, tissueType, isTFactors, elevated):
        if (isTFactors == False):
            self.tissueTypeFile = tissueType
            if (elevated == True):
                self.epath = "Elevated Tissue/"
            else: 
                self.epath = "TissueFiles/"
            self.data = pd.DataFrame(data = pd.read_table(os.path.join(os.getcwd(), self.epath, self.tissueTypeFile), header=0,))
        else: 
            self.data = pd.DataFrame(data = pd.read_csv(os.path.join(os.getcwd(), 'DataBaseExtract_v_1.01.csv'), header=0,))
            self.formatCSV()
    """inputColumns accepts an array of columns found in TissueTypes."""
    def returnColumnData(self, inputColumns):   
        return self.data.get(inputColumns, default="NA")
    def returnAllData(self):
        return self.data
    def popColumns(self, inputColumns):
        self.data.droplevel(inputColumns)
    def formatCSV(self):
        self.data.loc[:, "Ensembl ID"]
        self.data.rename(columns = {"Ensembl ID": "Ensembl"}, inplace=True)
    def alignTwoSets(self, dataset):
        left, right = self.data.align(dataset, index = 0)
        print (left)
        print (right)
        return left