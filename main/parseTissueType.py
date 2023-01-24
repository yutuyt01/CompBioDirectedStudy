import pandas as pd
import os

class tissueBase:
    def __init__(self, tissueType, isTFactors):
        if (isTFactors == False):
            self.tissueTypeFile = tissueType
            self.data = pd.DataFrame(data = pd.read_table(os.path.join('C:/Users/shang/OneDrive/Documents/Comp Bio 2022-23/CompBioDirectedStudy/TissueFiles/', self.tissueTypeFile), header=0,))
        else: 
            self.data = pd.DataFrame(data = pd.read_csv('C:/Users/shang/OneDrive/Documents/Comp Bio 2022-23/CompBioDirectedStudy/DataBaseExtract_v_1.01.csv', header=0,))
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